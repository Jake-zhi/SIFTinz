from time import clock

from ReadImage import ReadImage
from Read_Mask import ReadMask

from SaveImage import SaveImage


__author__ = 'Agnieszka'

import numpy as np


class LocalExterma3D(object):
    def __init__(self, path, path_mask='', flag=False):
        """
        Find local extrema without edges in one image
        """
        self.flag = flag
        self.path_mask = path_mask
        self.mask = ReadMask(path_mask).openMask()
        self.true_array = np.ones((3, 3, 3), dtype=np.bool)
        self.false_array = -self.true_array
        self.true_array[1, 1, 1] = False

        self.min_list = []
        self.max_list = []
        self.path = path
        self.ReadImage = ReadImage(path)

    def find_one(self, image3D):
        """
        :param image3D: DoG Image as Image object
        :return: void
        """
        self.min_list = []
        self.max_list = []
        image3D = image3D.Image3D
        shape = image3D.shape
        start = clock()
        for i in range(1, shape[0]):
            for j in range(1, shape[1]):
                for z in range(1, shape[2]):
                    if self.flag == True and self.mask.sum_mask[i, j, z]==0:
                        continue # this is fast version

                    bool_array = image3D[i, j, z] > image3D[i - 1:i + 2, j - 1:j + 2, z - 1:z + 2]
                    sum = np.sum(bool_array)
                    if sum == 0:
                            self.min_list.append(np.array([i, j, z]))

                    elif sum == 26 and bool_array[1, 1, 1] == False:
                            self.max_list.append(np.array([i, j, z]))
        print(len(self.max_list), len(self.min_list))
        end = clock() - start
        print end

    def find(self):
        list_with_images = self.ReadImage.openImage()
        path_to_save = '/3DLocalExtremum/'
        saving = SaveImage(self.path + path_to_save)
        saving.saveImage(list_with_images[0])
        saving.saveImage(list_with_images[len(list_with_images) - 1])
        for i in range(1, len(list_with_images) - 1):
            self.find_one(list_with_images[i])
            min3D, max3D = self.get_min_max()

            print(min3D.shape, max3D.shape)
            list_with_images[i].keypoints_min = min3D
            list_with_images[i].keypoints_max = max3D
            saving.saveImage(list_with_images[i])
            print('image nr' + str(i) + 'done')


    def get_min_max(self):
        """
        :return: list of indexes as a np.array min and max [i,j,z]
        """
        return np.array(self.min_list), np.array(self.max_list)