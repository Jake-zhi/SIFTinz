from Image import Image3D

__author__ = 'Agnieszka'

import os
import warnings

__author__ = 'Agnieszka'
import numpy as np
from os import walk
from os.path import join

import cPickle as pickle


class ReadImage(object):
    def __init__(self, path):
        self.path = path
        self.ImagesList = []

    def openImage(self):
        if not os.path.exists(self.path):
            raise IOError
        files_in_dir = [join(self.path, fn) for fn in next(walk(self.path))[2]]
        for f in files_in_dir:
            print(f)
            if '.ct' in f:
                try:

                    file_temp = file(f, 'rb')
                    temp_file = np.load(file_temp)
                    im = Image3D(temp_file['image'], temp_file['spacing'], temp_file['width'], temp_file['high'],
                                 temp_file['depth'], temp_file['sigma'], temp_file['keypoints_min'],
                                 temp_file['keypoints_max'],temp_file['keypoints_orientation'],temp_file['discriptor'])
                    self.ImagesList.append(im)

                finally:
                    file_temp.flush()
                    file_temp.close()
            else:
                Warning(f + ' wrong file- probably not npy file')
                return self.ImagesList
        return self.ImagesList
        print('Reading data done')


