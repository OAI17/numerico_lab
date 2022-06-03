import numpy as np 
from matplotlib import pyplot as plt

def intenumcomp(fun,a,b,N,regla):

    if regla == "trapecio":
        trapecio(fun,a,b,N)
    
    elif regla == "pm":
        pm(fun,a,b,N)
    
    elif regla == "simpson":
        simpson_compuesta(fun,a,b,N)

    else:
        print("Operacion incorrecta")
        #intenumcomp(fun,a,b,N,regla)

def trapecio(fun,a,b,N):
    #Integra hasta pol de grado 1#
    xj = np.linspace(a,b,N+1)
    h = (b-a)/N

    derivada_seg = 1

    error = abs(-(((b-a)/12)*(h**2) * derivada_seg))
    
    print(f"El error en trapecio es {error}")

def pm(fun,a,b,N):
    #Integra hasta pol de grado 1#
    assert(N % 2 == 0)

    h = ((b-a)/(N+2))
 
    derivada_seg = 1

    error = abs(-(((b-a)/6)*(h**2) * derivada_seg))
    
    print(f"El error en pm es {error}")
    
def simpson_compuesta(fun,a,b,N):
    #Integra hasta pol de grado 3#
    
    h = (b-a)/N

    derivada_seg = 1

    error = abs(-(((h**4)/180) * derivada_seg))
    
    print(f"El error en simpson es {error}")
    

fun = lambda x: np.exp(-x)
interval = [4,10,20]
for i in range(len(interval)):
    intenumcomp(fun,0,1,interval[i],"simpson")
    intenumcomp(fun,0,1,interval[i],"pm")
    intenumcomp(fun,0,1,interval[i],"trapecio")
    print("-----------------------------------")