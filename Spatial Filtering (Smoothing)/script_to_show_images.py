# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:37:05 2020

@author: chetan
"""


import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('lena.jpg', 0)
img1 = cv2.imread('mean_7x7.jpg', 0)
img2 = cv2.imread('mean_15x15.jpg', 0)
img3 = cv2.imread('gauss7x7.jpg', 0)
img4 = cv2.imread('gauss15x15.jpg', 0)

fig = plt.figure()
fig.set_figheight(15)
fig.set_figwidth(15)

fig.add_subplot(3,2,1)
plt.title('original image')
plt.imshow(img, cmap='gray')


fig.add_subplot(3,2,2)
plt.title('mean 7x7 image')
plt.imshow(img1, cmap='gray')


fig.add_subplot(3,2,3)
plt.title('mean 15x15 image')
plt.imshow(img2, cmap='gray')


fig.add_subplot(3,2,4)
plt.title('gauss 7x7 image')
plt.imshow(img3, cmap='gray')

fig.add_subplot(3,2,5)
plt.title('gauss 15x15 image')
plt.imshow(img4, cmap='gray')

plt.show(block=True)