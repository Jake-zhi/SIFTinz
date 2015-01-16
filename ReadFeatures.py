import os
from os.path import join
from Masks import keyPoints_in_organ

__author__ = 'Agnieszka'
import numpy as np
class ReadMask(object):
    def __init__(self, path):
        self.path = path

    def openMask(self):
        features=0
        if not os.path.exists(self.path):
            raise IOError
        files_in_dir = [join(self.path, fn) for fn in next(os.walk(self.path))[2]]

        for f in files_in_dir:
            print(f)
            if 'features' in f:
                try:

                    file_temp = file(f, 'rb')
                    temp_file = np.load(file_temp)
                    mask = keyPoints_in_organ(temp_file['prostate_key'], temp_file['bladder_key'], temp_file['rectum_key'], temp_file['femurR_key'],
                                 temp_file['femurL_key'], temp_file['semi_vesicle_key'])


                finally:
                    file_temp.flush()
                    file_temp.close()
            else:

                Warning(f + ' wrong file- probably not mask file')

        return features
        print('Reading data done')