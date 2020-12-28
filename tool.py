import os
import sys
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 
def initial():
    path = os.getcwd()
    if not os.path.exists('picture'):
        os.mkdir('picture')
        print('Please input your data')
        exit()
    if not os.path.exists('MuellerMatrix'):
        os.mkdir('MuellerMatrix')
        os.chdir('MuellerMatrix')
        if not os.path.exists('polar_decomposition'):
            os.mkdir('polar_decomposition')
        else:
            pass
        if not os.path.exists('differential_decomposition'):
            os.mkdir('differential_decomposition')
        else:
            pass
    else:
        pass
    os.chdir(path)
def imageread(filename_extension):
    path = 'picture'
    image0 = np.array(cv.imread(path + '/0.'+filename_extension,2),dtype=float)
    pr =int(image0.shape[1]/2)
    #裁切圖片
    image_range = int(input("請輸入預計解析度 = "))
    min_piexl_X = int(pr-image_range/2)
    min_piexl_Y = int(pr-image_range/2)
    max_piexl_X = int(pr+image_range/2)
    max_piexl_Y = int(pr+image_range/2)
    data0 = image0[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]
    data1 = np.array(cv.imread(path + '/1.'+filename_extension ,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data2 = np.array(cv.imread(path + '/2.'+filename_extension ,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data3 = np.array(cv.imread(path + '/3.' +filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data4 = np.array(cv.imread(path + '/4.' +filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data5 = np.array(cv.imread(path + '/5.' +filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data6 = np.array(cv.imread(path + '/6.' +filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data7 = np.array(cv.imread(path + '/7.' +filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data8 = np.array(cv.imread(path + '/8.' +filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data9 = np.array(cv.imread(path + '/9.' +filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data10 = np.array(cv.imread(path + '/10.'+filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data11 = np.array(cv.imread(path + '/11.'+filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data12 = np.array(cv.imread(path + '/12.'+filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data13 = np.array(cv.imread(path + '/13.'+filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data14 = np.array(cv.imread(path + '/14.'+filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data15 = np.array(cv.imread(path + '/15.'+filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data16 = np.array(cv.imread(path + '/16.'+filename_extension,2),dtype=float)[min_piexl_Y:max_piexl_Y,min_piexl_X:max_piexl_X]-data0
    data = np.array([data0,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16],dtype=float)
    return data
def export(typex,data,name,path):
    plt.imshow(data,cmap='jet')
    plt.title(name)
    if typex == 0:
        plt.clim(0,1)
    elif typex ==-1 :
        plt.clim(-1,1)
    elif typex == 90 :
        plt.clim(-90,90)
    elif typex == 180:
        plt.clim(-180,180)
    else:
        pass
    plt.axis('off')
    plt.colorbar()
    plt.savefig('MuellerMatrix\\'+path+'\\'+name+'.png')
    plt.close()
    return 'finsh'
def im_show(typex,data,name):
    plt.imshow(data,cmap='jet')
    plt.title(name)
    if typex == 0:
        plt.clim(0,1)
    elif typex ==-1 :
        plt.clim(-1,1)
    elif typex == 90 :
        plt.clim(-90,90)
    elif typex == 180:
        plt.clim(-180,180)
    else:
        pass
    plt.axis('off')
    plt.colorbar()
    plt.show()
    plt.close()
    return 'finsh'