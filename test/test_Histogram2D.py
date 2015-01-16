from math import pi
from matplotlib.pyplot import figure, imshow, show, colorbar
from numpy import ones, max, min
from Histogram2D import Histogram2D
from keypointOrientation import KeyPointOrientation
from readDicom import ReadDirWithBinaryData
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import unittest


class Histogram2DTest(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/'
        self.Dicoms = ReadDirWithBinaryData(self.path)
        self.spacing = self.Dicoms.get_spacing()

        self.keypointorientation = KeyPointOrientation(self.spacing, 1)
        path = './test_data/1_nd/npy_arrays_3DDoG/'
        self.ReadImage = ReadNumpy(path)
        self.list_of_image = self.ReadImage.openImage()
        self.ReadIndex = ReadNumpy('./test_data/1_nd/Hessian3D/')
        self.list_index = self.ReadIndex.openIndex()
        self.histogram = Histogram2D(4, 8)
        self.e, self.a, self.w = self.keypointorientation.keypoints_histograms(self.list_index[0][1],
                                                                               self.list_of_image[1])
        self.histogram.apply(self.e, self.a, self.w)

    def test_apply(self):
        self.histogram.apply(self.e, self.a, self.w)


    def test_getHistogram(self):
        H = self.histogram.get_Histogram2D()
        fig = figure(figsize=(7, 3))
        ax = fig.add_subplot(131)
        ax.set_title('imshow: equidistant')
        im = imshow(H, interpolation='None', origin='low')
        colorbar()
        show()

    def test_getHistogram_max(self):
        self.assertEqual(self.histogram.get_Histogram2D_max()[0][0], 0)
        self.assertEqual(self.histogram.get_Histogram2D_max()[0][1], 90)


if __name__ == '__main__':
    unittest.main()
