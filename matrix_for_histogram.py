from scipy.interpolate import interpn

from Histogram2D import Histogram2D
from Normalization import normalize
from Vizualization import visualization3D_notimage


__author__ = 'Agnieszka'

import numpy as np


class matrixHist(object):
    def __init__(self, mask_shape):
        '''
        :param spacing: spacing after rotation in mm
        :param mask_shape: shape of mask for histogram default is [15,15,15] in pixel and (16)mm after interpolation
         'for future changing in code structure'
        :return:void
        '''
        self.spacing = []
        self.mask_shape = mask_shape
        sigma_x = self.mask_shape * 1.5
        # sigma_z = self.mask_shape[2] * 1.5
        x_range = np.arange(0, self.mask_shape / 2 + 1)
        self.pixel_distance_x = np.sort(np.concatenate((-x_range[1:], x_range)))
        # z_range = np.arange(0, self.mask_shape / 2 + 1)
        # self.pixel_distance_z = np.sort(np.concatenate((-z_range[1:], z_range)))

        # maska poprawna co do wartosci!
        self.X, self.Y, self.Z = np.meshgrid(self.pixel_distance_x, self.pixel_distance_x,
                                             self.pixel_distance_x)

        self.gaussian_weight = np.exp(
            -((self.X ** 2 + self.Y ** 2 + self.Z ** 2) / (2 * (sigma_x ** 2))))
        self.magnitude = []
        self.weights = []

    def interp(self, mask, spacing):
        '''
        :param mask: new mask in space of 7.5 mm around keypoint
        :param spacing :spacing after interpolation
        :return: mask after interpolation
        '''
        self.spacing = spacing
        # new grid in mm in range of 15 mm from 0-8 mm, with points on a cross in a ceneter of mask

        new_grid_range_x = np.arange(0, self.mask_shape / 2 + 1, 1)
        new_pixel_distance_x = np.sort(np.concatenate((-new_grid_range_x[1:], new_grid_range_x)))
        # new_pixel_distance_z = np.sort(np.concatenate((-new_grid_range_x[1:], new_grid_range_x)))
        # grid from mask in mm after rotate, spacing under consideration grid is irregular
        print(spacing)
        grid_range_x = np.arange(0, ((mask.shape[0] / 2.) * self.spacing[0]), self.spacing[0])
        grid_range_y = np.arange(0, ((mask.shape[1] / 2.) * self.spacing[1]), self.spacing[1])
        grid_range_z = np.arange(0, ((mask.shape[2] / 2.) * self.spacing[2]), self.spacing[2])

        pixel_distance_x = np.sort(np.concatenate((-grid_range_x[1:], grid_range_x)))
        pixel_distance_y = np.sort(np.concatenate((-grid_range_y[1:], grid_range_y)))
        pixel_distance_z = np.sort(np.concatenate((-grid_range_z[1:], grid_range_z)))
        print(pixel_distance_x.max(),pixel_distance_y.max(),pixel_distance_z.max())
        print(new_grid_range_x.max())
        x, y, z = np.meshgrid(new_pixel_distance_x, new_pixel_distance_x, new_pixel_distance_x, indexing='ij')
        interpolate_grid = np.array([x[:, :, :], y[:, :, :], z[:, :, :]]).T



        new_mask = interpn((pixel_distance_x, pixel_distance_y, pixel_distance_z ), mask, interpolate_grid,
                           bounds_error=True, fill_value=np.float32(0.0))

        return new_mask.T

    def apply(self, mask, spacing):
        mask = self.interp(mask, spacing)
        # constant for histogram
        delta_azimuth = np.pi / 4.
        delta_elevation = np.pi / 4.
        # mesurmet for histogram
        dx, dy, dz = np.gradient(mask)
        magnitude = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        azimuth = np.arctan2(dy, dx) + np.pi
        elevation = np.arctan2(dz, np.sqrt(dx ** 2 + dy ** 2)) + np.pi / 2
        # weights with normalization for equal contribution
        # solid_angle = 1 / (delta_elevation * (np.cos(azimuth) - np.cos(azimuth + delta_azimuth)))
        # solid_angle = normalize(solid_angle, [np.min(solid_angle), np.max(solid_angle)], [0, 1])
        self.magnitude = normalize(magnitude, [np.min(magnitude), np.max(magnitude)], [0, 1])
        self.gaussian_weight = normalize(self.gaussian_weight, [np.min(self.gaussian_weight),
                                                                np.max(self.gaussian_weight)], [0, 1])
        weights = magnitude * self.gaussian_weight  # * solid_angle
        self.weights = normalize(weights, [np.min(weights), np.max(weights)], [0, 1])
        # splitig array mask for 8 equal parts
        div0 = np.array([8, ])
        div1 = np.array([7, ])
        # angles
        h0 = np.hsplit(azimuth, div0)[0]
        A_1 = np.vsplit(h0, div0)[0]  # 1
        A_2 = np.vsplit(h0, div0)[0]  # 2
        A_3 = np.vsplit(h0, div1)[1]  # 3
        A_4 = np.vsplit(h0, div1)[1]  #
        h1 = np.hsplit(azimuth, div1)[1]
        A_5 = np.vsplit(h1, div0)[0]  # 5
        A_6 = np.vsplit(h1, div0)[0]  # 6
        A_7 = np.vsplit(h1, div1)[1]  # 7
        A_8 = np.vsplit(h1, div1)[1]  # 8

        h0 = np.hsplit(elevation, div0)[0]
        E_1 = np.vsplit(h0, div0)[0]
        E_2 = np.vsplit(h0, div0)[0]
        E_3 = np.vsplit(h0, div1)[1]  # 3
        E_4 = np.vsplit(h0, div1)[1]  #
        h1 = np.hsplit(elevation, div1)[1]
        E_5 = np.vsplit(h1, div0)[0]  # 5
        E_6 = np.vsplit(h1, div0)[0]  # 6
        E_7 = np.vsplit(h1, div1)[1]  # 7
        E_8 = np.vsplit(h1, div1)[1]  # 8
        # weights
        w0 = np.hsplit(self.weights, div0)[0]
        W_1 = np.vsplit(h0, div0)[0]  # 1
        W_2 = np.vsplit(h0, div0)[0]  # 2
        W_3 = np.vsplit(h0, div1)[1]  # 3
        W_4 = np.vsplit(h0, div1)[1]  #
        w1 = np.hsplit(self.weights, div1)[1]
        W_5 = np.vsplit(h1, div0)[0]  # 5
        W_6 = np.vsplit(h1, div0)[0]  # 6
        W_7 = np.vsplit(h1, div1)[1]  # 7
        W_8 = np.vsplit(h1, div1)[1]  # 8
        # constatn for histogram
        NO_xbin = 4
        NO_ybin = 8

        H2D = Histogram2D(NO_xbin, NO_ybin)
        list_of_histograms_for_keypoint = []
        for i in range(1, 9):
            nr = str(i)
            list_of_histograms_for_keypoint.append(
                H2D.get_Histogram2D(eval('E_' + nr), eval('A_' + nr), eval('W_' + nr)))
        # list of histograms for descriptor (8 histograms as 4x8 bins)
        return np.array(list_of_histograms_for_keypoint)





