from OpenMask import OpenMask
from Read_Mask import ReadMask
from Vizualization import visualization3D_notimage

__author__ = 'Agnieszka'

import unittest

class OpenMaskTest(unittest.TestCase):

    def test_init(self):
        OpenMask('./test_data/1_nd/')

    def test_read_mask(self):
        maski=ReadMask('D:/analiza_danych/DICOM/SIFT/data_1/CT_analyses/1/').openMask()
        visualization3D_notimage(maski.prostate)
