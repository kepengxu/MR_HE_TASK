import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('E:\\PyProject\\MR_HE_TASK\\org\\1.png')
grayimage=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow('image',image)

cv2.imshow('grayimage',grayimage)

cv2.waitKey(0)

kernel_8x4x1 = np.array([
    [1, 1, -1, -1],
    [1, 1, -1, -1 ],
    [1, 1, -1, -1 ],
    [1, 1, -1, -1 ],
    [-1,-1, 1, 1 ],
    [-1,-1, 1, 1 ],
    [-1,-1, 1, 1 ],
    [-1,-1, 1, 1 ]
])

paddingimage=np.zeros(shape=(grayimage.shape[0]+4,grayimage.shape[1]+2))

paddingimage[2:2+grayimage.shape[0],1:1+grayimage.shape[1]]=grayimage

for i in range(grayimage.shape[0]):
    for j in range(grayimage.shape[1]):
        t=abs(np.sum(kernel_8x4x1*grayimage[i:i+8,j:j+4]))
        paddingimage[i+2:i+6,j+1:j+3]=t




cv2.imshow('paddingimage',paddingimage)

cv2.waitKey(0)



# kernel = np.ones([12, 6], np.float32)/   #除以25是防止数值溢出
# dst = cv2.filter2D(image, -1, kernel)
# cv2.namedWindow('custom_blur_demo', cv2.WINDOW_NORMAL)
# cv2.imshow("custom_blur_demo", dst)
