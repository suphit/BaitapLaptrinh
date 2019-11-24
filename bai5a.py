# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 03:21:17 2019

@author: Suphit
"""



# 5.a ve ban co vua cac o den trang dan xen

import numpy as np
import matplotlib.pyplot as plt
covua = np.zeros((8,8))
covua[1::2, 0::2]=1
covua[0::2, 1::2]=1
plt.imshow(covua,cmap='binary')

plt.show()

