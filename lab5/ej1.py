from distutils.log import error
import numpy as np 
from matplotlib import pyplot as plt

'''
CONSIGNA
fun es la función de en a ser integrada, a, b ∈ son los extremos de integración,
N es la cantidad de subintervalos a usar y regla es un string, que deberá ser trapecio,
pm o simpson. La salida S debe ser un número real
'''

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
    f_a = fun(a)
    f_b = fun(b)
    
    f_xj = 0

    for j in range(1,len(xj)-1):
        f_xj = f_xj + fun(xj[j])


    error = ((b-a)/12)*(h**2) # Faltaria acotar la parte de la derivada

    integral = ((h/2) * (f_a + 2*f_xj + f_b)) - error
    print(f"Resultado de la integral de {a} hasta {b} es {integral} con metodo de trepecio compuesta")

def pm(fun,a,b,N):
    #Integra hasta pol de grado 1#
    assert(N % 2 == 0)

    h = ((b-a)/(N+2))
    
    xj = []
    for j in range(-1,N+2):
        xj.append(a + ((j+1)*h))
       
    f_x2j = 0
    
    for j in range(0,int(N/2)+1):
        f_x2j = f_x2j + fun(xj[j])
    
    error = ((b-a)/6)*(h**2) # Faltaria acotar la parte de la derivada

    integral = ((2*h) * f_x2j) - error
    print(f"Resultado de la integral de {a} hasta {b} es {integral} con metodo de pm compuesta")
    
def simpson_compuesta(fun,a,b,N):
    #Integra hasta pol de grado 3#
    xj = np.linspace(a,b,(N*2)+1)
    h = (b-a)/(2*N)

    error = ((h**5)/90)
    integral = 0 # Faltaria acotar la parte de la derivada

    for j in range(0,int(len(xj)/2)):
        pos_x0 = (2*j)-2
        pos_x1 = (2*j)-1
        pos_x2 = (2*j)
        integral = integral + ((h/3)*(fun(xj[pos_x0]) + (4*fun(pos_x1)) + fun(pos_x2)) - error)


    print(f"Resultado de la integral de {a} hasta {b} es {integral} con metodo de simpson compuesta")

#fun = lambda x: np.exp(x)
fun = lambda x: x
intenumcomp(fun,0,2,4,"simpson")

