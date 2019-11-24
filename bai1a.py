import math
import numpy as np 
import matplotlib.pyplot  as plt 

f= 60.0
fs=1000
T=1 / f 
N=5
A = 3 
t= np.arange(0,N*T, N*T/float(fs))
s1= 3* np.sin(2*math.pi * f* t)
plt.plot(t, s1, label='đồ thị tín hiệu s1 ')
plt.savefig('s1.png', dpi=300, bbox_inches='tight')
plt.show()