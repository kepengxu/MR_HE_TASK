import cv2
import numpy as np

def guideFilter(I, p, winSize, eps, s):
    # 输入图像的高、宽
    h, w = I.shape[:2]

    # 缩小图像
    size = (int(round(w * s)), int(round(h * s)))
    small_I = cv2.resize(I, size, interpolation=cv2.INTER_CUBIC)
    small_p = cv2.resize(I, size, interpolation=cv2.INTER_CUBIC)

    # 缩小滑动窗口
    X = winSize[0]
    small_winSize = (int(round(X * s)), int(round(X * s)))

    # I的均值平滑 p的均值平滑
    mean_small_I = cv2.blur(small_I, small_winSize)
    mean_small_p = cv2.blur(small_p, small_winSize)

    # I*I和I*p的均值平滑
    mean_small_II = cv2.blur(small_I * small_I, small_winSize)
    mean_small_Ip = cv2.blur(small_I * small_p, small_winSize)


    var_small_I = mean_small_II - mean_small_I * mean_small_I
    cov_small_Ip = mean_small_Ip - mean_small_I * mean_small_p

    small_a = cov_small_Ip / (var_small_I + eps)
    small_b = mean_small_p - small_a * mean_small_I


    mean_small_a = cv2.blur(small_a, small_winSize)
    mean_small_b = cv2.blur(small_b, small_winSize)

    # 放大
    size1 = (w, h)
    mean_a = cv2.resize(mean_small_a, size1, interpolation=cv2.INTER_LINEAR)
    mean_b = cv2.resize(mean_small_b, size1, interpolation=cv2.INTER_LINEAR)

    q = mean_a * I + mean_b

    return q

import os
method='guideblur'

sourcedir='/home/cooper/PycharmProjects/MR_HE_TASK/org'
targetdir='/home/cooper/PycharmProjects/MR_HE_TASK/out'

imagename='1.png'
imagenamelist=['1.png','2.png','3.png','4.png','5.png','6.png']
for imagename in imagenamelist:

    if not os.path.exists(targetdir+'/'+method):
        os.mkdir(targetdir+'/'+method)
    outputpath=targetdir+'/'+method+'/'+imagename
    image=cv2.imread(sourcedir+'/'+imagename)
    # image=cv2.bilateralFilter(image,0,80,7)/255.0
    image=image/255.0
    i=image

    image=guideFilter(i,image,(5,5),0.01,1.0)
    image=np.array(image*255,np.uint8)
    cv2.imwrite(outputpath,image)
