from SaveImage import SaveImage
from Vizualization import visualization3D, visualization3D_notimage
from matrix_for_histogram import matrixHist

__author__ = 'Agnieszka'
from scipy.interpolate import griddata
import numpy as np
from scipy.ndimage import affine_transform, rotate


def rotate_matrix(azimuth, elevation):
    """
    :param azimuth: in radians
    :param elevation: in radians
    :return: transformation matrix
    """
    return np.array([[np.cos(azimuth) * np.cos(elevation), -np.sin(azimuth), -np.cos(azimuth) * np.sin(elevation)],
                     [np.sin(azimuth) * np.cos(elevation), np.cos(azimuth), -np.sin(azimuth) * np.sin(elevation)],
                     [np.sin(elevation), 0, np.cos(elevation)]])


def rotation(matrix_size, azimuth, elevation):
    """
    not for using
    :param matrix_size:X
    :param azimuth:X
    :param elevation:X
    :return:X
    """
    rotate_m = rotate_matrix(azimuth, elevation)
    rotated = []
    pixel = []
    for i in range(-matrix_size, matrix_size + 1, 1):
        for j in range(-matrix_size, matrix_size + 1, 1):
            for z in range(-int(matrix_size / 10), int(matrix_size / 10) + 1, 1):
                pixel.append(np.array([i, j, z]))
                rotated.append(np.dot(np.array([i, j, z]), rotate_m))
    # rotated.append(np.dot(np.array([512, 512, 74]), rotate_m))
    return np.array(rotated), np.array(pixel)


import time


class rotateImage(object):
    def __init__(self, Image3D, size_of_area, path):
        '''
        rotation for every keypoint
        :param Image3D: image object after keypoint orientation
        :param size_of_area: 2*size of area in extra direction shape+4*size of area
        :return:void
        '''
        self.path = path
        self.image3D = Image3D
        self.size_of_area = size_of_area
        self.histograms = []
        self.path_to_save = '/Descriptor3D/'

    def apply(self):
        '''

        :return:
        '''
        list_keypoints = self.image3D.keypoints_orientation
        matrixH = matrixHist(15)

        saving = SaveImage(self.path + self.path_to_save)
        print(list_keypoints.shape)
        for keypoint in list_keypoints:
            mask, spacing = self.apply_for_keypoint(keypoint)
            print(mask.shape)
            self.histograms.append(matrixH.apply(mask, spacing))
        print len(self.histograms)
        self.image3D.discriptor = np.array(self.histograms)
        saving.saveImage(self.image3D)


    def apply_for_keypoint(self, keypoint):
        '''

        :param keypoint: one keypoint from orientation
        :return: part of image after rotation , spacing
        '''
        # localization

        azimuth = keypoint[4]
        elevation = keypoint[3]
        key_point = np.array(keypoint[0:3])
        # image for rotation
        twice_size_of_area = 2 * self.size_of_area
        area_begin = key_point[0] - self.size_of_area
        area_end = key_point[0] + self.size_of_area + 1
        area_begin_y = key_point[1] - self.size_of_area
        area_end_y = key_point[1] + self.size_of_area + 1
        area_begin_z = key_point[2] - np.ceil(self.size_of_area / (self.image3D.spacing[2] / self.image3D.spacing[1]))
        area_end_z = key_point[2] + np.ceil(self.size_of_area / (self.image3D.spacing[2] / self.image3D.spacing[1])) + 1

        if (area_begin < 0 or area_begin_y < 0) or (
                    (area_begin_z < 0 or area_end > self.image3D.Image3D.shape[0] - 1) or
                    (area_end_y > self.image3D.Image3D.shape[1] - 1 or area_end_z > self.image3D.Image3D.shape[2] - 1)):
            temp_im = np.zeros(np.array([self.image3D.Image3D.shape[0] + 2 * twice_size_of_area,
                                         self.image3D.Image3D.shape[1] + 2 * twice_size_of_area,
                                         self.image3D.Image3D.shape[2] + 2 * twice_size_of_area]), dtype=np.float32)

            key_point_temp = key_point + 2 * self.size_of_area
            temp_im[twice_size_of_area:temp_im.shape[0] - twice_size_of_area,
            twice_size_of_area:temp_im.shape[1] - twice_size_of_area,
            twice_size_of_area:temp_im.shape[2] - twice_size_of_area] = self.image3D.Image3D

            area_begin = key_point_temp[0] - self.size_of_area
            area_end = key_point_temp[0] + self.size_of_area + 1
            area_begin_y = key_point_temp[1] - self.size_of_area
            area_end_y = key_point_temp[1] + self.size_of_area + 1
            area_begin_z = key_point_temp[2] - np.ceil(
                self.size_of_area / (self.image3D.spacing[2] / self.image3D.spacing[1]))
            area_end_z = key_point_temp[2] + np.ceil(
                self.size_of_area / (self.image3D.spacing[2] / self.image3D.spacing[1])) + 1

            Image3D = temp_im[area_begin:area_end, area_begin_y:area_end_y, area_begin_z:area_end_z]

        else:
            Image3D = self.image3D.Image3D[area_begin:area_end, area_begin_y:area_end_y, area_begin_z:area_end_z]



        # roatation

        transform = rotate_matrix(azimuth, elevation)

        x = np.array([0, 0, Image3D.shape[2] - 1]).dot(transform.T)
        y = np.array([0, Image3D.shape[1] - 1, 0]).dot(transform.T)
        z = np.array([Image3D.shape[0] - 1, 0, 0]).dot(transform.T)
        spacing = np.array([self.image3D.spacing[0], self.image3D.spacing[1], self.image3D.spacing[2]]).dot(transform.T)
        if (np.abs(spacing) < 0.2).sum() > 0:
            index = np.abs(spacing) < 0.2
            spacing[index] = self.image3D.spacing[index]

        s = np.abs(x) + np.abs(y) + np.abs(z) + 1
        offset = 0.5 * (np.array([Image3D.shape[0], Image3D.shape[1], Image3D.shape[2]]) - 1) - (0.5 * s).dot(transform)

        # hack nearest zastepuje prolemy na brzegach nie do ominiacia jezeli obrocimy wiekszy obszar i wytniemy z niego srodek unikamy problemu
        s=np.ceil(s)
        if s[0] % 2 == 0:

            s[0] += 1
        if s[1] % 2 == 0:

            s[1] += 1
        if s[2] % 2 == 0:
            s[2] += 1
        print(s)
        dst = affine_transform(Image3D, transform.T, order=0, offset=offset, output_shape=s, cval=0,
                               output=np.float32)

        return dst, np.abs(spacing)



