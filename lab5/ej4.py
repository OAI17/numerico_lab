from re import A
from ej1 import *
import numpy as np 

#trapecio(fun,a,b,N,error)
#simpson_compuesta(fun,a,b,N,error)

def generic(a,b,fun,nt,ns):
    trapecio(fun,a,b,nt,0)
    
    if ns % 2 != 0: 
        simpson_compuesta(fun,a,b,ns+1,0)
    else:
        simpson_compuesta(fun,a,b,ns,0)
    print("---------------------")
fun1 = lambda x : x * np.exp(-x)
a, b = 0, 1

#eja
generic(a,b,fun1,130,7)

