from images_features import KeypointsFeatures

__author__ = 'Agnieszka'



import unittest


class KeypointsFeaturesCase(unittest.TestCase):
    def setUp(self):
        keypoints_path = './test_data/1_nd/CT_analyses/Descriptor3D/'
        mask_path = './test_data/1_nd/CT_analyses/'
        self.keydis=KeypointsFeatures(keypoints_path, mask_path)

    def test_something(self):
        self.keydis.apply()


if __name__ == '__main__':
    unittest.main()
