from ReadImage import ReadImage
from SaveImage import SaveImage
from Vizualization import visualization3D
from readDicom import ReadDirWithBinaryData

__author__ = 'Agnieszka'

import unittest


class ImageTest(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/'
        image = ReadDirWithBinaryData(self.path)
        self.image = image.get_image_aggregation()

    def test_SaveImage(self):
        SaveImage(self.path+'CT_analyses/').saveImage(self.image)

    def test_ReadImage(self):
        im = ReadImage(self.path+'CT_analyses/').openImage()
        visualization3D(im[0])