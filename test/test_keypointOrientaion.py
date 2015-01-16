from math import pi

from matplotlib import cm
from matplotlib.pyplot import figure, imshow, colorbar
from matplotlib import cm
from matplotlib.pyplot import figure, show
from mpl_toolkits.mplot3d import Axes3D
from numpy import min, max
from ReadImage import ReadImage
from Vizualization import keypoints_vizualization, keypointsOrinetation_vizualization
from keypointOrientation import KeyPointOrientation
from readDicom import ReadDirWithBinaryData
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'
import unittest
import numpy as np


class KeyPointOrientationTest(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/CT_analyses'

        self.keypointorientation = KeyPointOrientation(self.path)
        self.keypointorientation.apply()


    def test_pixel_diff(self):
        self.assertEqual(-np.min(self.keypointorientation.X), np.max(self.keypointorientation.X))
        self.assertEqual(-np.min(self.keypointorientation.Z), np.max(self.keypointorientation.Z))
        print np.min(self.keypointorientation.X), np.max(self.keypointorientation.Z)

    def test_visualization(self):
      path = './test_data/1_nd/CT_analyses/KeyPointsOrientation/'
      list_with_images = ReadImage(path).openImage()
      for z in list_with_images:
        keypointsOrinetation_vizualization(z)


'''
    #testy na orientacje



    def test_vectors(self):
        self.keypointorientation = KeyPointOrientation(self.spacing, 1)
        self.keypointorientation.keypoints_histograms(self.list_index[0][0], self.list_of_image[1])

    def test_weights_vizualization(self):
        self.keypointorientation = KeyPointOrientation(self.spacing, 1.1)
        self.keypointorientation.keypoints_histograms(self.list_index[0][0], self.list_of_image[1])
        u = self.keypointorientation.azimuth
        v = self.keypointorientation.elevation
        w = self.keypointorientation.weights
        print max(w),min(w),pi
        #obj = quiver3d(w,u, v, line_width=3, scale_factor=1)
        #show()
'''

if __name__ == '__main__':
    unittest.main()
