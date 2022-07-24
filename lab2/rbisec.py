import math #math.copysign(a,b) devuelve el valor abs de a pero con el signo de b 
import matplotlib.pyplot as plt
from regex import B

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

        print(f"Iteraciones {k},punto medio {c},funcion en c {f_c}")
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


#Ejemplo de demostracion
from matplotlib import pyplot as plt
import numpy as np
fun = lambda x : (x**2)

xs = np.linspace(0, 2, num=200)
f = (xs**2)
plt.plot(xs,f)
xn, yn = rbisec(fun,[0,1],-1e10,50)
plt.scatter(xn[-1],yn[-1],label=f"{xn[-1],yn[-1]}")
plt.legend()
plt.show()



def fun_lab2ej2a(x):
    valor = math.tan(x)-(2*x)
    return valor

def fun_lab2ej2b(x):
    valor = (x**2)-3
    return valor 

#hx,hy = rbisec(fun_lab2ej2a,[0.8, 1.4],1e-5, 100)
#hx,hy = rbisec(fun_lab2ej2b,[1, 4],1e-5, 100)
 
def grafica_a():
    x =range(-1,2)
    plt.plot(x, [fun_lab2ej2a(i) for i in x])
    plt.plot([-1,2],[0,0])
    #plt.axis([xmin,xmax,ymin,ymax]) escala de x e y 
    #plt.grid(True) te hace cuadro
    plt.show()

def grafica_b():
    x =range(0,5)
    plt.plot(x, [fun_lab2ej2b(i) for i in x])
    plt.show()
#grafica_b()
#grafica_a()


