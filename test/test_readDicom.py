__author__ = 'Agnieszka'

import unittest
from readDicom import ReadDirWithDicom

class readDicomTest(unittest.TestCase):

    def setUp(self):
        self.Dicoms=ReadDirWithDicom('./test_data')

    def test_get_all_slices_in_3D(self):
        self.assertEqual(self.Dicoms.get_all_slices_in_3D().shape, (512, 512, 11))

    def test_readWrongDir(self):
        try:
            ReadDirWithDicom('./hbjdcnjdjc')
        except StopIteration:
            pass
        else:
            self.fail('Did not see StopIteration')

    def test_readWrongFile(self):
        try:
            ReadDirWithDicom('./test_data_error')
        except IOError:
            pass
        else:
            self.fail('Did not see StopIteration')


if __name__ == '__main__':
    unittest.main()