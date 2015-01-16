import cPickle as pickle
import os
from numpy import savez

__author__ = 'Agnieszka'


class SaveImage(object):
    def __init__(self, path):
        self.path = path
        try:
            os.makedirs(path)
        except OSError:
            pass

    def saveImage(self, image):

        outfile = open(self.path + str(image.sigma) + '.ct', 'wb')

        print('file is saving')
        savez(outfile, image=image.Image3D, sigma=image.sigma, spacing=image.spacing, width=image.width,
              high=image.high,
              depth=image.depth, keypoints_min=image.keypoints_min, keypoints_max=image.keypoints_max,keypoints_orientation=image.keypoints_orientation,
              discriptor=image.discriptor)
        outfile.flush()
        outfile.close()
        print('file is saved')