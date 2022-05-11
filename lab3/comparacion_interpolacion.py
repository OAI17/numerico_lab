import math
from newton_interpola import inewton
from matplotlib import pyplot as plt


hx = []
hy = []

fun = lambda x : 1/(1 + 25*(x**2))

def dist(a,b):
    hz = []
    j = a
    while j <= b:
        hz.append(j)
        j += 0.01
         
        hx.append(j)
        hy.append(fun(j))

    return hz

def func_a(n): 
    hxi = []
    hyi = []

    for i in range(1,n+1):
        xi = ((2*(i-1))/n) -1
        fxi = fun(xi)
    
        hxi.append(xi)
        hyi.append(fxi)

    return hxi,hyi

def func_b(n):
    hxi = []
    hyi = []

    for i in range(1,n+1):
        xi = math.cos(((2*i+1)/(2*n+2))*math.pi)
        fxi = fun(xi)
    
        hxi.append(xi)
        hyi.append(fxi)

    return hxi,hyi

def grafica_a():
    fig, axs = plt.subplots(layout='constrained')

    for n in range(1,16):
        hxi, hyi = func_a(n)
        hz = dist(-1,1)
        hw = inewton(hxi,hyi,hz)
        axs.plot(hz,hw, label=n)

    axs.plot(hx,hy, label="fun_acion")
    axs.set_ylim(-5,5)
    axs.set_xlim(-1,1)
    axs.legend()
    plt.show()

def grafica_b():
    fig, axs = plt.subplots(layout='constrained')

    for n in range(1,16):
        hxi, hyi = func_b(n)
        hz = dist(-1,1)
        hw = inewton(hxi,hyi,hz)
        axs.plot(hz,hw, label=n)

    axs.plot(hx,hy, label="fun_acion")
    axs.set_ylim(-5,5)
    axs.set_xlim(-1,1)
    axs.legend()
    plt.show()

'''
Notar que con mas "informacion" es decir con mas puntos de datos interpola mejor a la funcion pero en un intervalo muy preciso, porque despues se vuelve inestable
'''