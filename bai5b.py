# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 08:39:16 2019

@author: Suphit
"""

import random
import numpy as np
import matplotlib.pyplot as plt
x,y = np.meshgrid(np.arange(8),np.arange(8)) 
chieucao = np.random.randint(0,64,(8,8)) 
plt.gca(aspect=1,xlim=[-1,8],ylim=[-1,8])
plt.scatter(x,y,c=chieucao,s=600,marker='s',cmap='RdPu') 
plt.colorbar()
plt.show()
