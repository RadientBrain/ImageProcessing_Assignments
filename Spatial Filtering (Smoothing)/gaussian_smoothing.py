# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:24:08 2020

@author: chetan
"""


import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
from convolution import convolution
 
# formula for Univariate Normal Distribution
def dnorm(x, mu, sd):
    return 1 / (np.sqrt(2 * np.pi) * sd) * np.e ** (-np.power((x - mu) / sd, 2) / 2)
 
 
def gaussian_kernel(size, sigma=1):
    kernel_1D = np.linspace(-(size // 2), size // 2, size)
    for i in range(size):
        kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)
    kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)
 
    kernel_2D *= 1.0 / kernel_2D.max()
 
    return kernel_2D
 
 
def gaussian_blur(image, kernel_size):
    kernel = gaussian_kernel(kernel_size, sigma=math.sqrt(kernel_size))
    return convolution(image, kernel, average=True)
 
 
if __name__ == '__main__':
    
    image = cv2.imread('lena.jpg',0)
 
    gauss1 = gaussian_blur(image, 7)
    cv2.imwrite('gauss7x7.jpg',gauss1)
    
    
    gauss2 = gaussian_blur(image, 15)
    cv2.imwrite('gauss15x15.jpg',gauss2)