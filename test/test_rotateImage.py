import math
import numpy
from numpy.testing import assert_array_almost_equal
from ReadImage import ReadImage
from Vizualization import visualization3D
from rotateImage import rotateImage

__author__ = 'Agnieszka'

import unittest


class rotateImageTest(unittest.TestCase):
    def setUp(self):
        self.open = ReadImage('./test_data/1_nd/CT_analyses/KeyPointsOrientation/').openImage()
        self.rotate = rotateImage(self.open[0],10,'./test_data/1_nd/CT_analyses/')

    def test_apply(self):
        import time
        c=time.clock()
        self.rotate.apply()
        print(c-time.clock())
    def test_roatation(self):
        '''
        im = self.rotate.apply(2*math.pi, 2*math.pi, 25)
        self.assertEqual(None,assert_array_almost_equal(im,self.open[0].Image3D[246:266, 246:266, 35:39],decimal=16))
        for i in range(0,20):
            for j in range(0,20):
                for z in range(0,4):
                    if(im[i,j,z]!=self.open[0].Image3D[246:266, 246:266, 35:39][i,j,z]):
                        print(im[i,j,z],self.open[0].Image3D[246:266, 246:266, 35:39][i,j,z])
        '''



    def test_visualiation(self):

        i=0
        j=0
        im,s= self.rotate.apply_for_keypoint([0,0,0,i*math.pi/4.0,j*math.pi/4.0])

        self.open[1].Image3D = im
        self.open[1].spacing=s

        visualization3D(self.open[1])






if __name__ == '__main__':
    unittest.main()
'''
        self.grid, self.pixel_index = rotation(size_of_area, azimuth, elevation)

        x = key_point[0]
        y = key_point[1]
        z = key_point[2]

        step_x = self.image3D.spacing[0]
        step_y = self.image3D.spacing[1]
        step_z = self.image3D.spacing[2]


        self.pixel_index[:, 0] = self.pixel_index[:, 0] + x
        self.pixel_index[:, 1] = self.pixel_index[:, 1] + y
        self.pixel_index[:, 2] = self.pixel_index[:, 2] + z
        #print(np.max(self.grid[:, 0]),np.max(self.grid[:, 1]),np.max(self.grid[:, 2]))
        self.grid[:, 0] = self.grid[:, 0] + x
        self.grid[:, 1] = self.grid[:, 1] + y
        self.grid[:, 2] = self.grid[:, 2] + z
        #self.grid[:, 0] = self.grid[:, 0]
        #self.grid[:, 1] = self.grid[:, 1]
        #self.grid[:, 2] = self.grid[:, 2] *step_z/step_y

        self.x, self.y, self.z = np.mgrid[-255:255, -255:255, -25:25]
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z
        self.x = self.x
        self.y = self.y
        #self.z = self.z *step_z/step_y

        #im = self.imageInterp()

        #print(np.max(self.grid[:, 0]),np.max(self.grid[:, 1]),np.max(self.grid[:, 2]))
        #print(np.min(self.grid[:, 0]),np.min(self.grid[:, 1]),np.min(self.grid[:, 2]))
        if(np.min(self.grid[:, 0])<0):
            s_x=abs(np.max(self.grid[:, 0]))+abs(np.max(self.grid[self.grid[:, 0]<0.0][:,0]))+1
        else: s_x=np.max(self.grid[:, 0])+1
        if(np.min(self.grid[:, 1])<0):
            s_y=abs(np.max(self.grid[:, 1]))+abs(np.max(self.grid[self.grid[:, 1]<0.0][:,1]))+1
        else: s_y=np.max(self.grid[:, 1])+1
        if(np.min(self.grid[:, 2])<0):
            s_z=abs(np.max(self.grid[:, 2]))+abs(np.max(self.grid[self.grid[:, 2]<0.0][:,2]))+1
        else: s_z=np.max(self.grid[:, 2])+1
        print(s_x,s_y,s_z)

        Z=np.zeros((s_x,s_y,s_z))
        for i in range(0,self.pixel_index.shape[0]):
            a=self.grid[i]
            b=self.pixel_index[i]
            Z[self.grid[i, 0], self.grid[i, 1], self.grid[i, 2]]=self.image3D.get_image3D()[self.pixel_index[i, 0], self.pixel_index[i, 1], self.pixel_index[i, 2]]
            if np.sum(a<0)==0:
                if(a[0]<512) and a[1]<512 and a[2]<74 and b[0]<s_x and b[1]<s_y and b[2]<s_z:
                    T[self.pixel_index[i, 0], self.pixel_index[i, 1], self.pixel_index[i, 2]]=self.image3D.get_image3D()[self.grid[i, 0], self.grid[i, 1], self.grid[i, 2]]
'''