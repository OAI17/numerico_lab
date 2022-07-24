import numpy as np 

def mat_diagonal(A,b):
    sol = np.ones(len(b))
    for i in range(0,len(b)):
        sol[i] = b[i]/A[i,i] 
    return sol

def sum_trinf(i,A,x):
    suma = 0
    if i != 0:
        for j in range(0,i):
            suma = suma + A[i,j]*x[j]
            
    return suma
def soltrinf(A,b):
    n = len(b)
    sol = np.ones(n)
    for i in range(0,n):
        if A[i,i] != 0:
            sol[i] = (b[i] - sum_trinf(i,A,sol))/A[i,i]
        else:
            print("Error, la matriz no es singular")
            exit()
    return sol
'''
A = np.array([[1,0,0],
             [3,3,0],
             [1,2,3]])
b = np.array([1,2,3])
print(soltrinf(A,b))
'''
def sum_trsp(i,A,x,n):
    suma = 0
    for j in range(i+1,n):
        suma  = suma + A[i,j]*x[j]
    return suma

def soltrsup(A,b):
    n = len(b)
    sol = np.ones(n)
    for i in range(0,n):
        n_i = n-1-i
        if A[n_i,n_i] != 0:
            sol[n_i] = (b[n_i]-sum_trsp(n_i,A,sol,n)) / A[n_i,n_i]
        
        else:
            print("Error, la matriz no es singular")
            exit()
    return sol
'''
A = np.array([[1,2,3],
             [0,3,3],
             [0,0,3]])
b = np.array([1,2,3])
print(soltrsup(A,b))
'''