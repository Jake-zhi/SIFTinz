import os
from ReadImage import ReadImage
from SaveImage import SaveImage
from SavingNumpyImage import SavingImageAsNumpy
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import numpy as np


class HessianMatrix(object):
    def __init__(self, threshold):
        self.threshold = threshold
        self.threshold_sqr = threshold ** 2
        self.keypoints_list = []


    def HessianValues(self, image, keypoints):
        self.keypoints_list = []
        Image3D = image.Image3D
        self.spacing = image.spacing


        img_dx, img_dy, img_dz = np.gradient(Image3D, self.spacing[0], self.spacing[1], self.spacing[2])

        img_dxx, img_dxy, img_dxz = np.gradient(img_dx, self.spacing[0], self.spacing[1], self.spacing[2])
        img_dyx, img_dyy, img_dyz = np.gradient(img_dy, self.spacing[0], self.spacing[1], self.spacing[2])
        img_dzx, img_dzy, img_dzz = np.gradient(img_dz, self.spacing[0], self.spacing[1], self.spacing[2])

        n = []
        for keypoint in keypoints:
            i = keypoint[0]
            j = keypoint[1]
            z = keypoint[2]
            try:
                hessian = np.array([[img_dxx[i, j, z], img_dyx[i, j, z], img_dzx[i, j, z]],
                                    [img_dxy[i, j, z], img_dyy[i, j, z], img_dzy[i, j, z]],
                                    [img_dxz[i, j, z], img_dyz[i, j, z], img_dzz[i, j, z]]])
                Trace = np.trace(hessian)

                Det = np.linalg.det(hessian)

                det_p_2 = img_dxx[i, j, z] * img_dzz[i, j, z] - img_dyz[i, j, z] ** 2 + img_dxx[i, j, z] * img_dzz[
                    i, j, z] - img_dzz[i, j, z] ** 2 + img_dxx[i, j, z] * img_dyy[i, j, z] - img_dxy[i, j, z] ** 2
                try:
                    if Det != 0.0:
                        n.append(((Trace ** 3) / Det))
                        if ((Trace ** 3) / Det) >= (((2 * self.threshold + 1) ** 3) / self.threshold_sqr):
                            if Trace * Det > 0:
                                if det_p_2 > 0:
                                    self.keypoints_list.append(keypoint)
                except FloatingPointError:
                    pass
            except IndexError:

                pass
        print max(n), min(n),

        return self.get_key_points()

    def HessianElimination(self, path):
        """
        :param path: path to CT analyses folder
        :return:void saving images aggregator
        """

        path = path
        path_to_save = '/Hessian3D/'

        saving = SaveImage(path + path_to_save)
        ReadIm = ReadImage(path + '/3DDoG/DoGSpaceExtremum3D/')
        # ImagesDOG = ReadImage(path + '/3DDoG/').openImage()
        im = ReadIm.openImage()

        for i in range(0, len(im)):
            if im[i].keypoints_min.shape[0] != 0:
                im[i].keypoints_min = self.HessianValues(im[i], im[i].keypoints_min)

            if im[i].keypoints_max.shape[0] != 0:
                im[i].keypoints_max = self.HessianValues(im[i], im[i].keypoints_max)

            saving.saveImage(im[i])

    def get_key_points(self):
        return np.array(self.keypoints_list)
