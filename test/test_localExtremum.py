from numpy import array
from ReadImage import ReadImage
from Vizualization import keypoints_vizualization, visualization3D, keypointsOrinetation_vizualization
from localExtermum import LocalExterma3D


__author__ = 'Agnieszka'

import unittest


class LocalExtrema3DTest(unittest.TestCase):
    def setUp(self):
        path = './test_data/1_nd/CT_analyses/3DDoG/'
        path_mask = './test_data/1_nd/CT_analyses/'

        self.local_extrema = LocalExterma3D(path,path_mask,True)

    def test_find(self):
        self.image3D_after_log = self.local_extrema.find()

    def test_show(self):
        path = './test_data/1_nd/CT_analyses/3DDoG/3DLocalExtremum/'
        list_with_images = ReadImage(path).openImage()
        keypoints_vizualization(list_with_images[-2])
        for z in list_with_images:

            keypoints_vizualization(z)


if __name__ == '__main__':
    unittest.main()