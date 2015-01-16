from ReadImage import ReadImage
from Vizualization import keypoints_vizualization, visualization3D
from extramaSpace import ExtremaSpace3D
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import unittest


class ExtremaSpace3DTest(unittest.TestCase):
    def setUp(self):
        path = './test_data/1_nd/CT_analyses/3DDoG/3DLocalExtremum/'
        self.extrema = ExtremaSpace3D(path)

    def test_find(self):
        self.extrema.find()

    def test_show(self):
        path = './test_data/1_nd/CT_analyses/3DDoG/DoGSpaceExtremum3D/'
        list_with_images = ReadImage(path).openImage()
        keypoints_vizualization(list_with_images[-1])

        for z in list_with_images:
            keypoints_vizualization(z)
            #keypoints_vizualization(z)



if __name__ == '__main__':
    unittest.main()
