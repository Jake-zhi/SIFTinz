from Masks import keyPoints_in_organ
from Normalization import keypoints_concatenate
from ReadImage import ReadImage
from Read_Mask import ReadMask
from SaveFeatures import SaveFeatures
from SaveImage import SaveImage
import numpy as np
from Vizualization import keypoints_vizualization, visualization3D

__author__ = 'Agnieszka'


class KeypointsFeatures(object):
    def __init__(self, path_images, path_mask):
        self.images = ReadImage(path_images).openImage()
        self.masks = ReadMask(path_mask).openMask()
        self.Save = SaveImage(path_mask + '/FullFeature/')
        self.organs_names = ['rectum', 'prostate', 'bladder', 'femurL', 'femurR', 'semi_vesicle']
        self.SaveFeatures = SaveFeatures(path_mask + '/FullFeature/')

    def apply(self):
        for im in self.images:
            organs_dic = {}
            print im.sigma
            for organ in self.organs_names:

                #

                i = im.keypoints_orientation[:, 0:3].astype(dtype=np.int16)

                index = (eval('self.masks.' + organ)[i[:, 0], i[:, 1], i[:, 2]] > 0.1)

                key_orientation = im.keypoints_orientation[index]
                key_discriptor = im.discriptor[index]
                if index.sum() > 0:
                    f = []
                    for d,k in zip(key_discriptor,key_orientation):
                        f.append(np.concatenate((k,d.flatten())))
                    organs_dic[organ] = np.array(f)
                else:
                    organs_dic[organ] = np.array([])
                print(organs_dic[organ].shape)

            im.keypoints_orientation = organs_dic.values()[:][0]
            im.discriptor = organs_dic.values()[:][1]
            features = keyPoints_in_organ(organs_dic['prostate'], organs_dic['bladder'], organs_dic['rectum'],
                                          organs_dic['femurR'], organs_dic['femurL'], organs_dic['semi_vesicle'])
            self.SaveFeatures.saveFeatures(features, im.sigma)
            self.Save.saveImage(im)