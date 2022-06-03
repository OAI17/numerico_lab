import numpy as np 
from matplotlib import pyplot as plt

'''
CONSIGNA
fun es la función de en a ser integrada, a, b ∈ son los extremos de integración,
N es la cantidad de subintervalos a usar y regla es un string, que deberá ser trapecio,
pm o simpson. La salida S debe ser un número real
'''

def intenumcomp(fun,a,b,N,regla,error):

    if regla == "trapecio":
        trapecio(fun,a,b,N,error)
    
    elif regla == "pm":
        pm(fun,a,b,N,error)
    
    elif regla == "simpson":
        simpson_compuesta(fun,a,b,N,error)

    else:
        print("Operacion incorrecta")
        #intenumcomp(fun,a,b,N,regla)

def trapecio(fun,a,b,N,error):
    #Integra hasta pol de grado 1#
    xj = np.linspace(a,b,N+1)
    h = (b-a)/N
    f_a = fun(a)
    f_b = fun(b)
    
    f_xj = 0

    for j in range(1,len(xj)-1):
        f_xj = f_xj + fun(xj[j])

    integral = ((h/2) * (f_a + 2*f_xj + f_b)) - error
    print(f"Resultado de la integral de {a} hasta {b} es {integral} con metodo de trepecio compuesta")
    return integral
    
def pm(fun,a,b,N,error):
    #Integra hasta pol de grado 1#
    assert(N % 2 == 0)

    h = ((b-a)/(N+2))
    cota = int(N/2)+1
    sum = 0 

    for j in range(cota):
        sum = sum + (a+ fun(((2*j)+1)*h))

    integral = ((2*h) * sum) - error

    print(f"Resultado de la integral de {a} hasta {b} es {integral} con metodo de pm compuesta")
    
def simpson_compuesta(fun,a,b,N,error):
    #Integra hasta pol de grado 3#
    
    h = (b-a)/(2*N)

    sx_0 = fun(a) + fun(b)
    sx_1 = 0 
    sx_2 = 0 
    x = a

    for j in range(1,2*N):
        x = x + h

        if j % 2 == 0:
            sx_2 = sx_2 + fun(x)
        
        else:
            sx_1 = sx_1 + fun(x)
    
    sx = ((sx_0 + (2*sx_2) + (4*sx_1))*h )/3 - error

    print(f"Resultado de la integral de {a} hasta {b} es {sx} con metodo de simpson compuesta")

fun = lambda x: x**2    
#fun = lambda x: x
#intenumcomp(fun,0,2,4,"simpson",0)
#intenumcomp(fun,0,2,4,"pm",0)
#intenumcomp(fun,0,2,4,"trapecio",0)

