import os
from DoG import DoG
from GaussianSmoothing import GaussianSmoothing3D
from HessianMatrix import HessianMatrix
from OpenMask import OpenMask
from ReadImage import ReadImage
from ResizeImage import ResizeImage3D
from extramaSpace import ExtremaSpace3D
from images_features import KeypointsFeatures
from keypointOrientation import KeyPointOrientation
from localExtermum import LocalExterma3D
from readDicom import ReadDirWithBinaryData
from rotateImage import rotateImage

__author__ = 'Agnieszka'


class SIFT3D(object):
    def __init__(self, path):
        self.path = path

    def SIFTgrain(self, octave):
        path_analyse = '/CT_analysesClassification/' + octave
        octaves = 6

        initial_sigma = 1.1
        gauss = GaussianSmoothing3D(self.path + path_analyse, octaves).smoothing(initial_sigma)
        dimension = 3

        dog = DoG(self.path + path_analyse, dimension)
        dog.apply()
        pathDoG = '/3DDoG/'
        local_extrema = LocalExterma3D(self.path + path_analyse + pathDoG, self.path + path_analyse, True)
        local_extrema.find()
        path_local_extrema = '/3DLocalExtremum/'
        extrema = ExtremaSpace3D(self.path + path_analyse + pathDoG + path_local_extrema)
        extrema.find()
        Hessian = HessianMatrix(5.0)
        Hessian.HessianElimination(self.path + path_analyse)

        keypointorientation = KeyPointOrientation(self.path + path_analyse)
        keypointorientation.apply()
        path_keypoint_orientation = '/KeyPointsOrientation/'
        images = ReadImage(self.path + path_analyse + path_keypoint_orientation).openImage()
        for im in images:
            rotateImage(im, 10, self.path + path_analyse).apply()

        path_discriptor = '/Descriptor3D/'
        keydis = KeypointsFeatures(self.path + path_analyse + path_discriptor, self.path + path_analyse).apply()

    def apply(self):
        # first scale

        self.Dicoms = ReadDirWithBinaryData(self.path)
        mask = OpenMask(self.path)
        self.SIFTgrain('1/')
        self.resize = ResizeImage3D(self.path + '/CT_analysesClassification/1/', 2).apply()
        self.SIFTgrain('2/')
        self.resize = ResizeImage3D(self.path + '/CT_analysesClassification/2/', 3).apply()
        self.SIFTgrain('3/')


import time

if __name__ == '__main__':
    c = time.clock()
    for i in range(32, 43):
        try:
            path = 'D:/dane/' + str(i) + '_nd/'
            if not os.path.exists(path):
                raise IOError
        except IOError:
            continue
        sift = SIFT3D(path).apply()
    print(c - time.clock())



