import numpy as np 
from ej1 import soltrsup

def egauss(A,b):
    n = len(b)
    for k in range(0,n):
        for i in range(k+1, n):
            if A[k,k] ==  0:
                print("Error, la matriz es singular")
                exit()
            else:
                m = A[i,k] / A[k,k]

                for j in range(k+1,n):
                    A[i,j] = A[i,j]- (m*A[k,j])
                
                b[i] = b[i]- (m*b[k])
    return (A,b)

def soleg(A,b):
    U, x = egauss(A,b)
    return soltrsup(U,x)

'''
A = np.array([[1,2,1],
             [3,5,3],
             [2,2,4]])
b = np.array([1,2,3])
print(soleg(A,b))
'''