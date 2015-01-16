import unittest
from matplotlib.pyplot import imshow, show
import numpy
from DoG import DoG
from ReadImage import ReadImage
from Vizualization import visualization2D, visualization3D
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'
from numpy import max , min

class DoG2DTest(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/CT_analyses/'
        self.dog = DoG(self.path, 2)

    def test_smoothing(self):
        self.dog.apply()

    def test_min(self):
        path = './test_data/1_nd/CT_analyses/2DDoG/'
        self.ReadImage = ReadImage(path)
        list_of_image = self.ReadImage.openImage()
        for z in list_of_image:
            print min(z.Image3D),max(z.Image3D),z.sigma

    def test_show(self):
        path = './test_data/1_nd/CT_analyses/2DDoG/'
        self.ReadImage = ReadImage(path)
        list_of_image = self.ReadImage.openImage()
        for Z in list_of_image:
            visualization2D(Z.Image3D)


class DoG3DTest(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/CT_analyses/'
        self.dog = DoG(self.path, 3)

    def test_smoothing(self):
        self.dog.apply()

    def test_min(self):
        path = './test_data/1_nd/CT_analyses/3DDoG/'
        self.ReadImage = ReadImage(path)
        list_of_image = self.ReadImage.openImage()
        for z in list_of_image:
            print min(z.Image3D),max(z.Image3D),z.sigma

    def test_show(self):
        path = './test_data/1_nd/CT_analyses/3DDoG/'
        self.ReadImage = ReadImage(path)
        list_of_image = self.ReadImage.openImage()

        for Z in list_of_image:

            visualization3D(Z)


if __name__ == '__main__':
    unittest.main()
