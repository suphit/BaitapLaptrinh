import array as arr
import numpy as np
from scipy import linalg


print("Nhap vao n so: ")
n = int(input())
arr = [ float(input()) for i in range(n)]

print("Nhap vao m so: ")
m = int(input())
arr1 = [ float(input()) for i in range(m)]


k= m-n
i=0
while (i<k):
    
        arr.append(0)
        i +=1
    
arr=arr+arr
padding = np.zeros(len(arr) - 1, type(arr[0]))


first_col = np.r_[arr1, padding]
first_row = np.r_[arr1[0], padding]

H = linalg.toeplitz(first_col, first_row)

kq=np.dot(H, arr)


print(repr(kq))

t=np.arange(m,2*m)
result = np.copy(kq[t, ])

print(repr(result))
