from IOSift.FeatureReader import FeatureReader

__author__ = 'Agnieszka'

import unittest


class FeatureReaderTest(unittest.TestCase):
    def setUp(self):
        self.path = 'D:/dane/1_nd/CT_analysesClassification/2/FullFeature'
        self.feature_reader = FeatureReader(self.path)

    def test_open(self):
        self.feature_reader.open()

    def test_len(self):
        self.assertEqual(len(self.feature_reader.open()),3)


if __name__ == '__main__':
    unittest.main()
