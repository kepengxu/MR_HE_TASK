import cv2
import os
method='test_resize'

sourcedir='/home/cooper/PycharmProjects/MR_HE_TASK/org'
targetdir='/home/cooper/PycharmProjects/MR_HE_TASK/out'

imagename='1.png'
imagenamelist=['1.png','2.png','3.png','4.png','5.png','6.png']
for imagename in imagenamelist:

    if not os.path.exists(targetdir+'/'+method):
        os.mkdir(targetdir+'/'+method)
    outputpath=targetdir+'/'+method+'/'+imagename
    image=cv2.imread(sourcedir+'/'+imagename)
    print(image.shape)
    image=cv2.resize(image,(image.shape[1]*2,image.shape[0]*2))
    image=cv2.bilateralFilter(image,0,100,7)
    image=cv2.resize(image,(image.shape[1]//2,image.shape[0]//2))
    print(image.shape)
    # out=cv2.bilateralFilter(image,0,80,7)
    # cv2.imshow('image',image)
    # cv2.waitKey(0)
    cv2.imwrite(outputpath,image)
