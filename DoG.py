from Normalization import normalize
from ReadImage import ReadImage
from SaveImage import SaveImage

__author__ = 'Agnieszka'


class DoG(object):
    def __init__(self, path, dim):
        self.path = path
        if dim == 2:

            self.open_path = '2DGaussianSmoothing/'

            self.path_to_save = '/2DDoG/'
        elif dim == 3:
            self.open_path = '3DGaussianSmoothing/'
            self.path_to_save = '3DDoG/'
        else:
            raise (str(dim), "dimension is wrong")

        self.ReadImage = ReadImage(self.path + self.open_path)
        # make directory


    def apply(self):
        list_of_image = self.ReadImage.openImage()
        saving = SaveImage(self.path+self.path_to_save)
        import numpy as np
        for i in range(0, len(list_of_image)-1):

            DoG = list_of_image[i + 1].Image3D - list_of_image[i].Image3D
            print('before',np.min(DoG) ,np.max(DoG))
            DoG=normalize(DoG,[-1,1],[0,1])
            print(DoG.dtype)
            print(np.min(DoG) ,np.max(DoG))
            list_of_image[i].Image3D=DoG
            saving.saveImage(list_of_image[i])