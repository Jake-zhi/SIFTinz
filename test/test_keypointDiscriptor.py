from keypointDiscriptor import KeypointsDiscard

__author__ = 'Agnieszka'

import unittest


class KeypointsDiscardCase(unittest.TestCase):
    def setUp(self):
        keypoints_path = './test_data/1_nd/CT_analyses/Descriptor3D/'
        mask_path = './test_data/1_nd/CT_analyses/'
        self.keydis=KeypointsDiscard(keypoints_path, mask_path)

    def test_something(self):
        self.keydis.apply()


if __name__ == '__main__':
    unittest.main()
