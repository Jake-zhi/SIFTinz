from ReadImage import ReadImage
from ResizeImage import ResizeImage3D

__author__ = 'Agnieszka'
import unittest


class ResizeImageTest(unittest.TestCase):
    def setUp(self):
        self.resize = ResizeImage3D('./test_data/1_nd/CT_analyses/', 2)

    def test_a(self):
        self.resize.apply()
