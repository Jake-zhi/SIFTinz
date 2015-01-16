import os
from os.path import join
from Masks import Masks

from Save_mask import SaveMask
from Vizualization import visualization3D, visualization3D_notimage

__author__ = 'Agnieszka'
import numpy as np


class OpenMask(object):
    def __init__(self, path):
        """
            :param path: path to data containing data for one patient
            :return:void
            """
        self.my_path = path
        # read sizing
        meta_bin = open(self.my_path + 'hdr_CT.bin.txt')
        self.width = int(meta_bin.readline().split(' = ')[1][:-2])
        self.high = int(meta_bin.readline().split(' = ')[1][:-2])
        self.depth = int(meta_bin.readline().split(' = ')[1][:-2])
        self.data_type = meta_bin.readline().split(' = ')[1][:-2]
        # read image
        if not os.path.exists(self.my_path):
            raise IOError
        files_in_dir = [join(self.my_path, fn) for fn in next(os.walk(self.my_path))[2]]
        mask_dict = {}
        for f in files_in_dir:
            print(f)
            if 'mask' in f:
                try:
                    l = open(str(f), "rb")
                    mask_array = (np.array(np.fromfile(l, dtype="<i1")))
                    organ = str(l).split('_mask')[0].split('/')[-1]
                    print(organ)
                    mask_dict[organ] = np.reshape(mask_array, (self.width, self.high, self.depth), order='F')


                finally:
                    l.flush()
                    l.close()
        else:
            Warning(f + ' wrong file- probably not npy file')

        self.mask_agregation = Masks(mask_dict['prostate'], mask_dict['bladder'], mask_dict['rectum'],
                                     mask_dict['femurR'], mask_dict['femurL'], mask_dict['semi_vesicle'])
        SaveMask(path + '/CT_analysesClassification/1/').saveMask(self.mask_agregation)
        print('Reading data done')
