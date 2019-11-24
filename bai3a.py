# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:57:09 2019

@author: Suphit
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def mausangdentrang(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

img = mpimg.imread('bird.png')     
gray = mausangdentrang(img)    
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()


