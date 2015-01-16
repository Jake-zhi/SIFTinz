from HessianMatrix import HessianMatrix
from ReadImage import ReadImage
from Vizualization import keypoints_vizualization
from readDicom import ReadDirWithBinaryData
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import unittest


class HessianMatrixTest3D(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/CT_analyses'
        self.Hessian = HessianMatrix(40.0)

    def test_HessianElimination(self):
        self.Hessian.HessianElimination(self.path)

    def test_show(self):
        path = './test_data/1_nd/CT_analyses/Hessian3D/'
        list_with_images = ReadImage(path).openImage()
        for z in list_with_images:
            keypoints_vizualization(z)


if __name__ == '__main__':
    unittest.main()
