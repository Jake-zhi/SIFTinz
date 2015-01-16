from math import ceil, pi
from ReadImage import ReadImage
from Read_Mask import ReadMask
from SaveImage import SaveImage


__author__ = 'Agnieszka'

import numpy as np
#nie zrobione!

class KeypointsDiscard(object):
    def __init__(self, path_images, path_mask):
        self.images = ReadImage(path_images).openImage()
        self.masks = ReadMask(path_mask).openMask()
        self.Save = SaveImage(path_mask + '/FullFeature/')

    def apply(self):
        for im in self.images:
            i = im.keypoints_orientation[:, 0:3].astype(dtype=np.int16)
            index = (self.masks.rectum[i[0], i[1], i[2]] == 1)
            print(index.sum())
            im.keypoints_orientation = im.keypoints_orientation[index]
            im.discriptor = im.discriptor[index]
            self.Save.saveImage(im)



