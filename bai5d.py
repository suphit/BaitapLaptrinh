# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 08:42:28 2019

@author: Suphit
"""
import numpy as np
import random
import matplotlib.pyplot as plt
x,y = np.meshgrid(np.arange(8),np.arange(8))
chieucao = np.random.randint(0,64,(8,8)) 
plt.gca(aspect=1,xlim=[-1,8],ylim=[-1,8])
plt.scatter(x,y,c=chieucao,s=600,marker='s',cmap='RdPu')
plt.colorbar()
plt.colorbar(orientation='horizontal')
plt.show()
