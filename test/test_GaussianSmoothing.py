from matplotlib.pyplot import imshow, show

from GaussianSmoothing import GaussianSmoothing3D, GaussianSmoothing2D
from ReadImage import ReadImage
from Vizualization import visualization3D


__author__ = 'Agnieszka'

import unittest


class Gauss3DTest(unittest.TestCase):
    def setUp(self):
        path = './test_data/1_nd/CT_analyses/'
        octaves = 6
        self.gauss = GaussianSmoothing3D(path, octaves)

    def test_smoothing(self):
        sigma = 1.1
        self.gauss.smoothing(sigma)

    def test_show(self):
        list_of_image = ReadImage('./test_data/1_nd/CT_analyses/3DGaussianSmoothing/').openImage()
        for Z in list_of_image:
            visualization3D(Z)


class Gauss2DTest(unittest.TestCase):
    def setUp(self):
        self.path ='./test_data/1_nd/CT_analyses/'
        octaves = 6
        self.gauss = GaussianSmoothing2D(self.path, octaves)

    def test_soothing(self):
        sigma = 1.1
        self.gauss.smoothing(sigma)

    def test_show(self):
        path = './test_data/1_nd/CT_analyses/2DGaussianSmoothing/'
        self.ReadImage = ReadImage(path)
        list_of_image = self.ReadImage.openImage()
        for Z in list_of_image:
            imshow(Z.Image3D, cmap='gray')
            show()


if __name__ == '__main__':
    unittest.main()
