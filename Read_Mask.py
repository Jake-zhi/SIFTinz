import os
from os.path import join
from wx import Mask
from Masks import Masks

__author__ = 'Agnieszka'
import numpy as np
class ReadMask(object):
    def __init__(self, path):
        self.path = path

    def openMask(self):
        mask=0
        if not os.path.exists(self.path):
            raise IOError
        files_in_dir = [join(self.path, fn) for fn in next(os.walk(self.path))[2]]

        for f in files_in_dir:
            print(f)
            if 'masks' in f:
                try:

                    file_temp = file(f, 'rb')
                    temp_file = np.load(file_temp)
                    mask = Masks(temp_file['prostate'], temp_file['bladder'], temp_file['rectum'], temp_file['femurR'],
                                 temp_file['femurL'], temp_file['semi_vesicle'],temp_file['sum_mask'])


                finally:
                    file_temp.flush()
                    file_temp.close()
            else:

                Warning(f + ' wrong file- probably not mask file')

        return mask
        print('Reading data done')