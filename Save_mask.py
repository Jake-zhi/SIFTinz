import os
from numpy import savez

__author__ = 'Agnieszka'


class SaveMask(object):
    def __init__(self, path):
        self.path = path
        try:
            os.makedirs(path)
        except OSError:
            pass

    def saveMask(self, mask):

        outfile = open(self.path + 'masks.bin', 'wb')

        print('file is saving')
        savez(outfile, prostate=mask.prostate, bladder=mask.bladder, rectum=mask.rectum, femurR=mask.femurR,
              femurL=mask.femurL, semi_vesicle=mask.semi_vesicle,sum_mask=mask.sum_mask)
        outfile.flush()
        outfile.close()
        print('file is saved')