
from SIFT.SIFT3D import SIFT3D

__author__ = 'Agnieszka'

import unittest


class SIFT3DTest(unittest.TestCase):
    def setUp(self):
        path = 'D:/dane/1_nd/'
        self.sift = SIFT3D(path)

    def test_apply(self):
        self.sift.apply()