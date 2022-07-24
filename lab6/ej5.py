import numpy as np 
from ej1 import sum_trinf,sum_trsp

def jacobi(A,b,x,mit,err):
    n = len(b)
    u = np.ones(n)
    for k in range(1,mit):
        for i in range(0,n):
            u[i] = (1/A[i,i])*(b[i]- sum_trinf(i,A,x) - sum_trsp(i,A,x,n))

        if max(abs(u-x)) < err:
            print(f"Ultima iteracion de GS: {k}")
            break

        for i in range(0,n):
            x[i] = u[i]
    print(f"Ultima iteracion de GS: {mit}")
    return x 

def gseidel(A,b,x,mit,err):
    n = len(b)
    for k in range(1,mit):
        u = np.zeros(n)

        for i in range(0,n):
            u[i] = (1/A[i,i]) * (b[i] - sum_trinf(i,A,u) - sum_trsp(i,A,x,n)) 
        
        if max(abs(u-x)) < err:
            print(f"Ultima iteracion de GS: {k}")
            break

        for i in range(0,n):
            x[i] = u[i]
    print(f"Ultima iteracion de GS: {mit}")
    return x 

#ej 6 (1)
A = np.array([[3,1,1],
             [2,6,1],
             [1,1,4]])
b = np.array([5,9,6])

x = np.array([9,2,-1]) #vector inicial

print(f"Metodo de jacobi {jacobi(A,b,x,1000,10e-11)}")
print(f"Metodo de GS {gseidel(A,b,x,1000,10e-11)}")
