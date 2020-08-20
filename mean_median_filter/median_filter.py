import numpy as np
import cv2

img = cv2.imread('CT14_shot.bmp')
img_or = cv2.imread('CT14_shot.bmp')
img = img.mean(2)

imgOut = np.zeros (img.shape, dtype = "uint8")
imgOut2 = np.zeros (img.shape, dtype = "uint8")


for i in range(1,img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
        value = int(img[i-1][j-1])+int(img[i-1][j+1])+int(img[i+1][j-1])+int(img[i-1][j-1])+int(img[i-1][j])+int(img[i+1][j])+int(img[i][j-1])+int(img[i][j+1])+int(img[i][j])
        M = []
        for k in range(3):
            for l in range(3):
                M.append(img[i-1+k%3,j-1+l%3])
        imgOut[i, j] = np.median(M)
        imgOut2[i, j] = value/9
        

err1 = 0.0
err2 = 0.0

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        err1 += (img[i, j] - imgOut[i, j]) ** 2
        err2 += (img[i, j] - imgOut2[i, j]) ** 2

size = img.shape[0] * img.shape[1]

mse1 = err1/(size)
mse2 = err2/(size)


cv2.imshow('median mse = ' + str(mse1), imgOut)
cv2.imshow('mean_ mse = ' + str(mse2), imgOut2)
cv2.imshow('original', img_or)
cv2.waitKey(0)



