import math
import numpy as np 
import matplotlib.pyplot as plt 

f= 60.0
fs=1000
T=1 / f 
N=5
A = 3 
n=3
s2=np.zeros(fs)
t= np.arange(0,N*T, N*T/float(fs))
for i in range(2*n+1):
    sa=(A* np.sin(2* math.pi*(2*i+1)*f*t))/((2*i+1)**2)
    s2+=sa

plt.plot(t, s2, label='đồ thị tín hiệu s2 ')
plt.savefig('s2.png', dpi=300, bbox_inches='tight')
plt.show()

