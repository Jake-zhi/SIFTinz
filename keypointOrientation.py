from math import ceil, pi
import warnings

from mayavi import mlab
from mayavi.tools.helper_functions import barchart
from mayavi.tools.show import show
from Histogram2D import Histogram2D
from Normalization import keypoints_concatenate, normalize
from ReadImage import ReadImage
from SaveImage import SaveImage

__author__ = 'Agnieszka'

import numpy as np

np.seterr(all='raise')


class KeyPointOrientation(object):
    def __init__(self, path):
        self.path = path
        path_for_keypoints = path + '/Hessian3D/'
        path_for_Gaussian = path + '/3DGaussianSmoothing'
        self.ImageReader = ReadImage(path_for_Gaussian)
        self.PointReader = ReadImage(path_for_keypoints)
        self.list_with_keyponits = self.PointReader.openImage()
        self.spacing = self.list_with_keyponits[0].spacing
        self.size_in_pixels_xy = 3
        sigma_x = self.size_in_pixels_xy*1.5  # list_with_keyponits[0].sigma * 2 mask size is 9


        x_range = np.arange(0, self.size_in_pixels_xy + 1)
        self.pixel_distance_x = np.sort(np.concatenate((-x_range[1:], x_range)))
        self.size_of_window_x = self.size_in_pixels_xy
        self.size_of_window_z = self.size_in_pixels_xy
        self.X, self.Y, self.Z = np.meshgrid(self.pixel_distance_x, self.pixel_distance_x,
                                             self.pixel_distance_x)
        # self.X, self.Y = np.meshgrid(self.pixel_distance_x, self.pixel_distance_x)
        # to dla 1.5 sigmy

        self.gaussian_weight = np.exp(-((self.X ** 2 + self.Y ** 2 + self.Z ** 2) / (2 * (sigma_x / 2) ** 2)))

    def apply(self):
        list_with_GaussianImages = self.ImageReader.openImage()
        self.SaveImage = SaveImage(self.path + '/KeyPointsOrientation/')
        for i in range(0, len(self.list_with_keyponits)):
            orientation = self.keypoints_histograms(list_with_GaussianImages[i + 1], self.list_with_keyponits[i])
            list_with_GaussianImages[i + 1].keypoints_orientation = orientation
            list_with_GaussianImages[i + 1].keypoints_min = self.list_with_keyponits[i].keypoints_min
            list_with_GaussianImages[i + 1].keypoints_max = self.list_with_keyponits[i].keypoints_max
            self.SaveImage.saveImage(list_with_GaussianImages[i + 1])


    def keypoints_histograms(self, image3D_agregator, keypooints_agregator):
        # diff in [mm space]
        dx, dy, dz = np.gradient(image3D_agregator.Image3D, image3D_agregator.spacing[0], image3D_agregator.spacing[1],
                                 image3D_agregator.spacing[2])

        keypoints = keypoints_concatenate(keypooints_agregator)

        # do konfigracji
        delta_azimuth = np.pi / 4.
        delta_elevation = np.pi / 4.
        #solid_azimuth=np.arange(0,2*np.pi+delta_elevation,delta_elevation)
        #solid_angle = 1.0 / (delta_elevation * (np.cos(solid_azimuth) - np.cos(solid_azimuth + delta_azimuth)))

        #solid_angle = normalize(solid_angle, [np.min(solid_angle), np.max(solid_angle)], [0, 1])

        keypoint_list = []

        for k in range(0, keypoints.shape[0]):
            try:
                i = keypoints[k][0]
                j = keypoints[k][1]
                z = keypoints[k][2]
            except IndexError:
                keypoint_list.append([0,0,0,0,0])
                pass
                continue



            temp_x = dx[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                     z - self.size_of_window_z:z + self.size_of_window_z + 1]

            temp_y = dy[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                     z - self.size_of_window_z:z + self.size_of_window_z + 1]

            temp_z = dz[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                     z - self.size_of_window_z:z + self.size_of_window_z + 1]

            if temp_x.shape[0] != 2 * self.size_in_pixels_xy + 1:  continue
            if temp_x.shape[1] != 2 * self.size_in_pixels_xy + 1:  continue
            if temp_x.shape[2] != 2 * self.size_in_pixels_xy + 1:  continue

            self.magnitude = np.sqrt(temp_x ** 2 + temp_y ** 2 + temp_z ** 2)
            self.azimuth = np.arctan2(temp_y, temp_x) + np.pi

            self.elevation = np.arctan2(temp_z,np.sqrt(temp_x ** 2 + temp_y ** 2))+np.pi/2


            self.magnitude = normalize(self.magnitude, [np.min(self.magnitude), np.max(self.magnitude)], [0, 1])

            self.gaussian_weight = normalize(self.gaussian_weight, [np.min(self.gaussian_weight),
                                                                    np.max(self.gaussian_weight)], [0, 1])

            weights = self.magnitude * self.gaussian_weight #* solid_angle
            self.weights = normalize(weights, [np.min(weights), np.max(weights)], [0, 1])

            NO_xbin = 4
            NO_ybin = 8

            H2D = Histogram2D(NO_xbin, NO_ybin)
            H2D.apply(self.elevation, self.azimuth, weights)
            #self.H2D = H2D.get_Histogram2D()
            #fig =figure()
            from mpl_toolkits.mplot3d import Axes3D
            #ax = fig.add_subplot(111,projection='3d')
            #barchart(H2D.H)

            #mlab.colorbar(nb_labels=2,label_fmt='%.1f')
            #show()
            angles = H2D.get_Histogram2D_max()
            if angles.size == 4:
                keypoint_list.append([i, j, z, angles[0][0], angles[0][1]])
                keypoint_list.append([i, j, z, angles[1][0], angles[1][1]])
            elif angles.size == 2:

                keypoint_list.append([i, j, z, angles[0][0], angles[0][1]])

        return keypoint_list






