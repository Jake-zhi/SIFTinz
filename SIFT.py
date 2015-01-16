import os, sys
from SIFT.SIFT3D import SIFT3D

__author__ = 'Agnieszka'





import time
def main(agrv):
    print(agrv)
    path = agrv[1:]

    if not os.path.exists(path):
        raise IOError
    sift = SIFT3D(path).apply()
if __name__ == '__main__':

    main(sys.argv)





