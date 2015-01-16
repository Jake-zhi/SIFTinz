from matplotlib.pyplot import imshow, show
from Vizualization import visualization3D, visualization2D

__author__ = 'Agnieszka'

import unittest
from readDicom import ReadDirWithBinaryData
from numpy import array, array_equal, max, min


class readDicomTest(unittest.TestCase):
    def setUp(self):
        self.Dicoms = ReadDirWithBinaryData('./test_data/1_nd/')

    def test_get_image3D(self):
        self.assertEqual(self.Dicoms.get_image3D().shape, (512, 512, 74))

    def test_get_spacing(self):
        print(self.Dicoms.get_spacing())
        self.assertEqual(True, array_equal(self.Dicoms.get_spacing(), array([0.9766, 0.9766, 5.0000])))


    def test_readWrongFile(self):
        try:
            ReadDirWithBinaryData('./test_data_error')
        except IOError:
            pass
        else:
            self.fail('Did not see StopIteration')

    def test_values(self):
        self.assertEqual(max(self.Dicoms.get_image3D()), 2639)
        self.assertEqual(min(self.Dicoms.get_image3D()), 0)

    def test_showImage2D(self):
        print self.Dicoms.get_image3D().shape
        import numpy as np


        Z = self.Dicoms.get_image3D()[:, :, 3]
        visualization2D(Z)

    def test_showImage3D(self):
        visualization3D(self.Dicoms)


if __name__ == '__main__':
    unittest.main()