import cv2
import os
method='gaussianblur'

sourcedir='/home/cooper/PycharmProjects/MR_HE_TASK/org'
targetdir='/home/cooper/PycharmProjects/MR_HE_TASK/out'

imagename='1.png'
imagenamelist=['1.png','2.png','3.png','4.png','5.png','6.png']
for imagename in imagenamelist:

    if not os.path.exists(targetdir+'/'+method):
        os.mkdir(targetdir+'/'+method)
    outputpath=targetdir+'/'+method+'/'+imagename
    image=cv2.imread(sourcedir+'/'+imagename)
    out=cv2.GaussianBlur(image,(5,5),0)
    cv2.imwrite(outputpath,out)
