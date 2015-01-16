from Image import Image3D
from SaveImage import SaveImage

__author__ = 'Agnieszka'

from os import walk
from os.path import join

import dicom
import numpy as np


class ReadDirWithDicom(object):
    def __init__(self, path):

        my_path = path
        files_in_dir = [join(my_path, fn) for fn in next(walk(my_path))[2]]
        image3D = []
        for f in files_in_dir:
            if ".IMA" in f:
                dicom_data_set = dicom.read_file(f)
                image3D.append(dicom_data_set.pixel_array)
            else:
                raise IOError('wrong file- probably not DICOM')
        self.Image3D = np.dstack(image3D)
        print('Reading data done')


    def get_all_slices_in_3D(self):
        return self.Image3D


class ReadDirWithBinaryData(object):
    def __init__(self, path):
        """
        :param path: path to data containing data for one patient
        :return:void
        """
        self.my_path = path
        #read sizing
        meta_bin = open(self.my_path + 'hdr_CT.bin.txt')
        self.width = int(meta_bin.readline().split(' = ')[1][:-2])
        self.high = int(meta_bin.readline().split(' = ')[1][:-2])
        self.depth = int(meta_bin.readline().split(' = ')[1][:-2])
        self.data_type = meta_bin.readline().split(' = ')[1][:-2]
        #read image
        l = open(self.my_path + 'CT.bin', "r")
        f = (np.array(np.fromfile(l, dtype="<f4")))
        self.Image3D = np.reshape(f, (self.width, self.high, self.depth), order='F')
        #hackig for weird binary values
        if np.max(self.Image3D) < 0.1:
            self.Image3D = self.Image3D.byteswap()
        #read spacing
        self.spacing = np.fromfile(self.my_path + 'spacing.txt', dtype=float, sep="    ")
        self.im_agregation=Image3D(self.Image3D,self.spacing,self.width,self.high,self.depth,0)
        SaveImage(path+'/CT_analysesClassification/1/').saveImage(self.im_agregation)
        print('Reading data done')

    def get_image3D(self):
        """
        :return: Image from binary data as np.array with size self.width, self.high, self.depth
        """
        return self.Image3D

    def get_spacing(self):
        """
        :return: return size of pixels in mm x|,y-,z /
        """
        return self.spacing
    def get_image_aggregation(self):
        """

        :return:Image aggregation object
        """

        return self.im_agregation