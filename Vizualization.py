from matplotlib.pyplot import imshow, show
from mayavi import mlab
from mayavi.tools.helper_functions import points3d
from numpy import concatenate, ones
from Normalization import keypoints_concatenate

__author__ = 'Agnieszka'


def visualization2D(image2D):
    """

    :param image2D: array with 2D image
    :return:void
    """
    imshow(image2D, cmap='gray')
    show()

def visualization3D_notimage(image3D):
    """
    :param image3D: image object from readDirWithBinaryDAta
    :return:
    """

    s=image3D
    src = mlab.pipeline.scalar_field(image3D)
    src.spacing=[1,1,5]
    src.update_image_data = (1,1,5)
    '''
    mlab.pipeline.image_plane_widget(src,
                                     plane_orientation='x_axes',
                                     slice_index=1,
                                    colormap='black-white'


    )
    mlab.pipeline.image_plane_widget(src,
                                     plane_orientation='z_axes',
                                     slice_index=1,
                                     colormap='black-white'


    )
    '''



    mlab.pipeline.iso_surface(src, contours=[0.5,1], opacity=1,colormap='black-white')

    mlab.outline()

    mlab.show()
def visualization3D(image3D):
    """
    :param image3D: image object from readDirWithBinaryDAta
    :return:
    """
    s=image3D.Image3D
    src = mlab.pipeline.scalar_field(image3D.Image3D)
    src.spacing = image3D.spacing
    src.update_image_data = True

    mlab.pipeline.image_plane_widget(src,
                                     plane_orientation='x_axes',
                                     slice_index=128,
                                     colormap='black-white'
    )
    mlab.pipeline.image_plane_widget(src,
                                     plane_orientation='z_axes',
                                     slice_index=35,
                                     colormap='black-white'

    )
    mlab.pipeline.image_plane_widget(src,
                                     plane_orientation='y_axes',
                                     slice_index=128,
                                     colormap='black-white'

    )
    print(image3D.Image3D.shape)
    #index = keypoints_concatenate(image3D)
    #mlab.points3d(index[:, 0]*image3D.spacing[0], index[:, 1]*image3D.spacing[0], index[:, 2]*image3D.spacing[2],scale_factor=4)

    #mlab.pipeline.iso_surface(src, contours=[s.min()+0.1*s.ptp(), ], opacity=0.5)
    print(0.1*s.ptp())
    mlab.pipeline.iso_surface(src, contours=[s.max()-1300, ],colormap='hsv')

    mlab.outline()

    mlab.show()


def keypoints_vizualization(Image3D):
    #print(Image3D.keypoints_max.shape[0], Image3D.keypoints_min.shape[0])

    index = keypoints_concatenate(Image3D)

    size=ones((index.shape[0]))
    print('wielkosc',index.shape)
    points3d(index[:, 0], index[:, 1], index[:, 2]*5,scale_factor=4)
    mlab.show()

def keypointsOrinetation_vizualization(Image3D):
    index = Image3D.keypoints_orientation
    size=ones((index.shape[0],1))
    points3d(index[:, 0], index[:, 1], index[:, 2], mode='point')
    #x=sin()*cos()
    mlab.show()
