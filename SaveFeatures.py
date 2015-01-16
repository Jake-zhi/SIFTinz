import os
from numpy import savez

__author__ = 'Agnieszka'


class SaveFeatures(object):
    def __init__(self, path):
        self.path = path
        try:
            os.makedirs(path)
        except OSError:
            pass

    def saveFeatures(self, features, sigma):

        outfile = open(self.path  + str(sigma) + 'features.bin', 'wb')

        print('file is saving')
        savez(outfile, prostate_key=features.prostate_keypoints, bladder_key=features.bladder_keypoints,
              rectum_key=features.rectum_keypoints, femurR_key=features.femurR_keypoints,
              femurL_key=features.femurL_keypoints, semi_vesicle_key=features.semi_vesicle_keypoints)
        outfile.flush()
        outfile.close()
        print('file is saved')