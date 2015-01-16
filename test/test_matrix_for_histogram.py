from numpy import zeros
from matrix_for_histogram import matrixHist

__author__ = 'Agnieszka'

import unittest


class matrix_for_histogramTest(unittest.TestCase):

    def setUp(self):

        self.mask = zeros((21, 21, 5))
        self.mask[1:5,3:6,4:]=250
        self.matrixH = matrixHist(15)

    def test_something(self):
        self.matrixH.apply(self.mask,[.7, .7, 5])


if __name__ == '__main__':
    unittest.main()
