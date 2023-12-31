# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fsMo-kJsKeYg2N2MBzBUTzqnrtmnthXK
"""

import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
def filter(img,filter_name):
   m, n = img.shape
   mask = np.ones([3, 3], dtype = int)
   img_new = np.zeros([m, n])
   if filter_name =='mean':
      mask=mask/9
      for i in range(1,m-1):
          for j in range(1,n-1):
            temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2]

            img_new[i, j] = temp
            img_new = img_new.astype(np.uint8)
   if filter_name=='median':
      for i in range(1,m-1):
        for j in range(1,n-1):
          temp = [img[i-1, j-1],img[i-1, j],img[i-1, j + 1],img[i, j-1],img[i, j],img[i, j + 1],img[i + 1, j-1],img[i + 1, j],img[i + 1, j + 1]]
          temp = sorted(temp)
          img_new[i, j]= temp[4]
   if filter_name=='sobelX':
        img_new = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
   if filter_name=='sobelY':
        img_new=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
   if filter_name=='laplacian':
        img_new = cv2.Laplacian(img,cv2.CV_64F,ksize=3)

   return img_new


img = cv2.imread('MRI.png',0)
mean=filter(img,'mean')
median=filter(img,'median')
sobelX=filter(img,'sobelX')
sobelY=filter(img,'sobelY')
laplacian=filter(img,'laplacian')
plt.figure(0)
plt.subplot(321)
plt.imshow(img, cmap = 'gray', vmin=0, vmax=255)
plt.title('original')
plt.axis('off')
plt.subplot(322)
plt.imshow(mean, cmap = 'gray', vmin=0, vmax=255)
plt.title('averaging')
plt.axis('off')
plt.subplot(323)
plt.imshow(median, cmap = 'gray', vmin=0, vmax=255)
plt.title('median')
plt.axis('off')
plt.subplot(324)
plt.imshow(sobelX, cmap = 'gray', vmin=0, vmax=255)
plt.title('sobelX')
plt.axis('off')
plt.subplot(325)
plt.imshow(sobelY, cmap = 'gray', vmin=0, vmax=255)
plt.title('sobelY')
plt.axis('off')
plt.subplot(326)
plt.imshow(laplacian, cmap = 'gray', vmin=0, vmax=255)
plt.title('laplacian')
plt.axis('off')

def filter2(img,filter_name):
   m, n = img.shape
   mask = np.ones([5, 5], dtype = int)
   img_new = np.zeros([m, n])
   if filter_name =='mean':
     mask=mask/25
     for i in range(2,m-2):
       for j in range(2,n-2):
         temp = img[i-2, j-2]*mask[0, 0]+img[i-2, j-1]*mask[0, 1]+img[i-2, j]*mask[0, 2]+img[i-2,j+1]*mask[0,3]+img[i-2,j+2]*mask[0,4]+img[i-1, j-2]*mask[1, 0]+ img[i-1, j-1]*mask[1, 1]+img[i-1, j]*mask[1, 2]+img[i-1, j+1]*mask[1, 3]+img[i-1, j+2]*mask[1, 4]+img[i, j-2]*mask[2, 0]+img[i, j-1]*mask[2, 1]+img[i, j]*mask[2, 2]+img[i, j-1]*mask[2, 3]+img[i, j-2]*mask[2, 4]+img[i+1, j-2]*mask[3, 0]+img[i+1, j-1]*mask[3, 1]+img[i+1, j]*mask[3, 2]+img[i+1, j+1]*mask[3,3]+img[i+1, j+2]*mask[3, 4]+img[i+2, j-2]*mask[4, 0]+img[i+2, j-1]*mask[4, 1]+img[i+2, j]*mask[4, 2]+img[i+2, j+1]*mask[4, 3]+img[i+2, j+2]*mask[4, 4]
         img_new[i, j] = temp
         img_new = img_new.astype(np.uint8)
   if filter_name=='median':
      for i in range(2,m-2):
        for j in range(2,n-2):
          temp = [img[i-2, j-2],img[i-2, j-1],img[i-2, j],img[i-2,j+1],img[i-2,j+2],img[i-1, j-2], img[i-1, j-1],img[i-1, j],img[i-1, j+1],img[i-1, j+2],img[i, j-2],img[i, j-1],img[i, j],img[i, j-1],img[i, j-2],img[i+1, j-2],img[i+1, j-1],img[i+1, j],img[i+1, j+1],img[i+1, j+2],img[i+2, j-2],img[i+2, j-1],img[i+2, j],img[i+2, j+1],img[i+2, j+2]]
          temp = sorted(temp)
          img_new[i, j]= temp[12]
          img_new = img_new.astype(np.uint8)
   return img_new

plt.figure(1)
plt.subplot(221)
plt.imshow(filter(img,'mean'), cmap = 'gray', vmin=0, vmax=255)
plt.title('mean 3x3')
plt.axis('off')

plt.subplot(222)
plt.imshow(filter2(img,'mean'), cmap = 'gray', vmin=0, vmax=255)
plt.title('mean 5x5')
plt.axis('off')

plt.subplot(223)
plt.imshow(filter(img,'median'), cmap = 'gray', vmin=0, vmax=255)
plt.title('median 3x3')
plt.axis('off')

plt.subplot(224)
plt.imshow(filter2(img,'median'), cmap = 'gray', vmin=0, vmax=255)
plt.title('median 5x5')
plt.axis('off')

mask = np.array([[1, 2, 1], [2, 16, 2], [1, 2, 1]])
mask = mask/28
m,n=img.shape
centering = np.zeros([m,n])
for i in range(1, m-1):
    for j in range(1, n-1):
        temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2]

        centering[i, j]= temp

        centering= centering.astype(np.uint8)

plt.figure(2)
plt.subplot(121)
plt.imshow(filter(img,'median'), cmap = 'gray', vmin=0, vmax=255)
plt.title('averaging 3x3')
plt.axis('off')

plt.subplot(122)
plt.imshow(centering, cmap = 'gray', vmin=0, vmax=255)
plt.title('centering 3x3')
plt.axis('off')