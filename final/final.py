import numpy as np
from matplotlib import pyplot as plt
import math

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

    #print(f"Resultado de la integral de {a} hasta {b} es {sx} con metodo de simpson compuesta")
    return sx 

def rbisec(fun,I,err,mit):
    hx = []
    hy = []

    a = I[0]
    b = I[1]

    if (a == 0):
        a = (a-b)
    elif (b == 0):
        b = (a-b)

    f_a = fun(a) 
    f_b = fun(b) 
    
    e = b-a
        
    #Busca la x*

    for k in range(1,mit):
        e = e/2
        c = (a + b)/2
        f_c = fun(c)

        #print(f"Iteraciones {k},punto medio {c},funcion en c {f_c}")
        hx.append(c)
        hy.append(f_c)
                
        if f_a * f_c > 0:
            a = c
            f_c = f_c
        
        elif f_a * f_c < 0:
            b = c
            f_c = f_c
        
        if (abs(e) < err) or (abs(f_c) < err):
            return (hx,hy)
    return (hx,hy)


def integral_simpson(x):
    fun = lambda y : 1/y
    integral = simpson_compuesta(fun,1,x,100,0) 
    return integral

#Lo primero que hice es graficar la funcion integral_simpson para tener una idea como es
#Para poder usar los metodos de raices tengo que restar uno para que la ec me quede igualada a 0
#Despues volvi a graficar y vi que cambia de signo en el intervalo [1,8], por lo que puedo usar biseccion

xs = np.linspace(1,8,num=100)

#grafica integral de integral_simpson
f = integral_simpson(xs)
plt.plot(xs,f,label="integral de simpson")   

#funcion que me sirve para encontrar la raiz y grafico
h = integral_simpson(xs)-1
plt.plot(xs,h,label="integral de simpson -1") 
#misma funcion pero adaptada para biseccion
g = lambda x : integral_simpson(x) -1

#devuelve los sucecivos intervalos y los grafico
x,y = rbisec(g,[1,8],1e-6,100)
sol = x[-1]
plt.scatter(x,y)
plt.scatter(x[-1],y[-1],color="red",label="ultima iteracion")

error = abs(math.e-sol) 
print(f"La aproximacion de e es {sol}")
print(f"El error absoluto de la aprox es {error}")

plt.legend()
plt.show()

 
