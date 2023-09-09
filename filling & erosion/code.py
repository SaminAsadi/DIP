# -*- coding: utf-8 -*-
"""HW5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1doJjTCcRK9ozewp3ccjyEccIJwdgj26U
"""

#4
import cv2 as cv
import numpy as np
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
#4.1)
image1=cv.imread('4_1.png')
image2=cv.imread('chopper.png')
#4.2)
#filling the holes
print(image1.shape)
kernel1 = np.ones((60, 60), np.uint8)
im_out=cv.morphologyEx(image1, cv.MORPH_CLOSE, kernel1)
# Taking a matrix of size 5 as the kernel
kernel2 = np.ones((10, 10), np.uint8)
img_erosion = cv.erode(im_out, kernel2, iterations=1)
# finding boundaries using erosion
B=im_out-img_erosion
plt.figure()
plt.subplot(121)
plt.imshow( image1)
plt.subplot(122)
plt.imshow( B)
#4.3)
Newimg=np.zeros((image1.shape),dtype=np.uint8)
def subtraction(img1,img2):
  Newimg=abs(img1-img2)
  return Newimg
newImage=subtraction(image1,image2)
plt.figure()
plt.subplot(131)
plt.imshow( image1)
plt.subplot(132)
plt.imshow( image2)
plt.subplot(133)
plt.imshow( newImage)
plt.title('subtracted image')
#4.4)
image=cv.imread('Blobs.png',0)
#4.5)
def ball(r):
  ball=cv.getStructuringElement(cv.MORPH_ELLIPSE,(r,r))
  return ball
closing= cv.morphologyEx(image, cv.MORPH_CLOSE, ball(55))
opening=cv.morphologyEx(closing, cv.MORPH_OPEN, ball(95))
erosion=cv.erode(opening, ball(30), iterations=1)
final_img=image-opening+erosion
plt.figure()
plt.subplot(321)
plt.imshow( image,cmap='gray',vmin=0,vmax=255)
plt.subplot(322)
plt.imshow( closing,cmap='gray',vmin=0,vmax=255)
plt.subplot(323)
plt.imshow( opening,cmap='gray',vmin=0,vmax=255)
plt.subplot(324)
plt.imshow( erosion,cmap='gray',vmin=0,vmax=255)
plt.subplot(338)
plt.imshow( final_img,cmap='gray',vmin=0,vmax=255)
#4.6)
print(image.shape)
def intensity(img):
   sum=0
   for i in range(599):
     for j in range(599):
       sum=sum+abs(img[i,j])
   return sum
print(intensity(image))


def ball_numbers(img):
  I=np.zeros((36),dtype=np.float64)
  j=0
  diff=img
  value=intensity(img)
  for i in range(30,65,1):
    diff=cv.morphologyEx(diff, cv.MORPH_OPEN, ball(i))
    value=(value-intensity(diff))
    I[j]=value
    j=j+1
  return I
# sequence of erosion plotting
plt.figure()
plt.subplot(231)
image1=cv.morphologyEx(image, cv.MORPH_OPEN, ball(35))
plt.imshow((image1),cmap='gray',vmin=0,vmax=255)
plt.axis('off')
plt.title('r=35')
plt.subplot(232)
image2=cv.morphologyEx(image, cv.MORPH_OPEN, ball(40))
plt.imshow( image2,cmap='gray',vmin=0,vmax=255)
plt.axis('off')
plt.title('r=40')
plt.subplot(233)
image3=cv.morphologyEx(image, cv.MORPH_OPEN, ball(45))
plt.imshow( image3,cmap='gray',vmin=0,vmax=255)
plt.axis('off')
plt.title('r=45')
plt.subplot(234)
image4=cv.morphologyEx(image, cv.MORPH_OPEN, ball(50))
plt.imshow(image4 ,cmap='gray',vmin=0,vmax=255)
plt.axis('off')
plt.title('r=50')
plt.subplot(235)
plt.imshow(cv.morphologyEx(image, cv.MORPH_OPEN, ball(55)),cmap='gray',vmin=0,vmax=255)
plt.axis('off')
plt.title('r=55')
plt.subplot(236)
plt.imshow(cv.morphologyEx(image, cv.MORPH_OPEN, ball(60)),cmap='gray',vmin=0,vmax=255)
plt.axis('off')
plt.title('r=60')