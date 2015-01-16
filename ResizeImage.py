from scipy.ndimage import zoom
from Masks import keyPoints_in_organ, Masks
from ReadImage import ReadImage
from Read_Mask import ReadMask
from SaveImage import SaveImage
from Save_mask import SaveMask

from Vizualization import visualization3D_notimage

__author__ = 'Agnieszka'


class ResizeImage3D(object):
    def __init__(self, path, octave_nd, resize_factor=0.5):
        """

        :param path:
        :param octave_nd:
        :param resize_factor:
        """
        self.octave_nd = octave_nd
        self.path = path
        self.resize_factor = resize_factor
        self.organs_names = ['rectum', 'prostate', 'bladder', 'femurL', 'femurR', 'semi_vesicle']

    def apply(self):
        organs_dic = {}
        masks = ReadMask(self.path).openMask()
        for organ in self.organs_names:
            organs_dic[organ] = zoom((eval('masks.' + organ)), self.resize_factor, order=1, mode='nearest',
                                     prefilter=True)

        new_masks = Masks(organs_dic['prostate'], organs_dic['bladder'], organs_dic['rectum'],
                          organs_dic['femurR'], organs_dic['femurL'], organs_dic['semi_vesicle'])
        SaveMask(self.path[:-2] + str(self.octave_nd) + '/').saveMask(new_masks)
        list_temp = ReadImage(self.path + '3DGaussianSmoothing').openImage()
        image3D = list_temp[int(len(list_temp) / 2.)]
        image3D.Image3D = zoom(image3D.Image3D, self.resize_factor, order=1, mode='nearest', prefilter=True)
        image3D.spacing=image3D.spacing*2.
        SaveIm = SaveImage(self.path[:-2] + str(self.octave_nd) + '/')
        SaveIm.saveImage(image3D)