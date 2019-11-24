# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 08:39:16 2019

@author: Suphit
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(64).reshape(8,8)
plt.figure(figsize=[8,8])
plt.imshow(x,cmap='RdPu')
plt.show()
