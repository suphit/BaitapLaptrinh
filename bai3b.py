# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:10:21 2019

@author: Suphit
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
bird = mpimg.imread('bird.png')
plt.subplot(221)
plt.imshow(bird)
plt.subplot(222)
plt.imshow(bird*np.array([1,0,0],dtype='uint8'))
plt.subplot(223)
plt.imshow(bird*np.array([0,1,0],dtype='uint8'))
plt.subplot(224)
plt.imshow(bird*np.array([0,0,1],dtype='uint8'))
plt.subplots_adjust(0.05,0.05,0.98,0.98,0.1,0.1)
plt.show()