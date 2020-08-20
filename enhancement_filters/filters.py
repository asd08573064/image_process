import numpy as np
import cv2

img = cv2.imread('CT14.bmp')
img_or = cv2.imread('CT14.bmp')
img = img.mean(2)

imgOut1 = np.zeros (img.shape, dtype = "uint8")
imgOut2 = np.zeros (img.shape, dtype = "uint8")
imgOut3 = np.zeros (img.shape, dtype = "uint8")
imgOut4 = np.zeros (img.shape, dtype = "uint8")

para1 = 1.2
para2 = 1.2


for i in range(1,img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
        value1 = -int(img[i-1][j])-int(img[i+1][j])-int(img[i][j-1])-int(img[i][j+1])+4*int(img[i][j])
        value4 = -int(img[i-1][j-1])-int(img[i-1][j+1])-int(img[i+1][j-1])-int(img[i-1][j-1])-int(img[i-1][j])-int(img[i+1][j])-int(img[i][j-1])-int(img[i][j+1])+8*int(img[i][j])
        value2 = -int(img[i-1][j-1])-int(img[i-1][j+1])-int(img[i+1][j-1])-int(img[i-1][j-1])-int(img[i-1][j])-int(img[i+1][j])-int(img[i][j-1])-int(img[i][j+1])+(9*para1-1)*int(img[i][j])
        value3 = -int(img[i-1][j-1])-int(img[i-1][j+1])-int(img[i+1][j-1])-int(img[i-1][j-1])-int(img[i-1][j])-int(img[i+1][j])-int(img[i][j-1])-int(img[i][j+1])+(9*para2-1)*int(img[i][j])
        imgOut1[i, j] = min(255, max(0, value1))
        imgOut2[i, j] = min(255, max(0, value2/para1/9))
        imgOut3[i, j] = min(255, max(0, value3/9))
        imgOut4[i, j] = min(255, max(0, value4))

cv2.imshow('laplace', imgOut1)
cv2.imshow('unsharp mask', imgOut2)
cv2.imshow('high-boost', imgOut3)
cv2.imshow('My Image original', img_or)
cv2.waitKey(0)

        
