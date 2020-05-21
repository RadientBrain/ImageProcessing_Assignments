# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:44:20 2020

@author: chetan
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np
from convolution import convolution
# =============================================================================
# #To rotate image 180 degrees 
# def conv_transform(image):
#     image_copy=image.copy()
#     for i in range (image.shape[0]):
#         for j in range(image.shape[1]):
#             image_copy[i][j] = image[image.shape[0]-i-1][image.shape[1]-j-1]
#     return image_copy
# =============================================================================

def conv(image,kernel,k):
    #kernel = conv_transform(kernel)
    image_h = image.shape[0]
    image_w = image.shape[1]
    
    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]
    
    h = kernel_h // 2
    w = kernel_w // 2
    
    image_conv = np.zeros(image.shape)
    
    for i in range(h, image_h-h):
        for j in range(w,image_w-w):
            sum = 0
            
            for m in range(kernel_h):
                for n in range(kernel_w):
                    sum = sum +((kernel[m][n] * image[i-h+m][j-w+n])//k)   
            image_conv[i][j]=sum
    
    return image_conv

img = cv2.imread('lena.jpg',0)

cv2.imshow('original',img)

#7x7 kernel
kernel1 = np.ones((7, 7), np.uint8) 

p = kernel1.shape[0]
q=p*p

new1=conv(img,kernel1,q)

#15x15 kernel
kernel2 = np.ones((15, 15), np.uint8) 

r = kernel2.shape[0]
s=r*r

new2=conv(img,kernel2,s)

cv2.imwrite('mean_7x7.jpg',new1)
loo_1= cv2.imread('mean_7x7.jpg', 0)

cv2.imshow('mean_filter7x7',loo_1)



cv2.imwrite('mean_15x15.jpg',new2)
loo_2= cv2.imread('mean_15x15.jpg', 0)

cv2.imshow('mean_filter15x15',loo_2)



cv2.waitKey(8000)
cv2.destroyAllWindows()

