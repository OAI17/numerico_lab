import numpy as np
from matplotlib import pyplot as plt


def a():

    data = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos3a.dat")

    hx = data[0]
    hy = data[1]

    m = len(hx)
    x = 0
    y = 0
    x_cuad = 0
    x_y = 0

    for i in range(0,m):
        x = x + float((hx[i]))
        y = y + float(np.log(hy[i]))
        x_cuad = x_cuad + (float(hx[i])**2)
        x_y = x_y + float((hx[i])*float(np.log(hy[i])))

    # ax + b
    B = (((x_cuad*y)-(x_y*x))/((m*x_cuad)-(x**2)))
    A = ((m*x_y)-(x*y))/((m*x_cuad)-(x**2))
    
    a = np.exp(A)
    b = np.exp(B)
    

    fun = b*(a**hx)

    plt.plot(hx,fun,label="Aproximacion",color="blue")
    plt.scatter(hx,hy,label="Datos",color="red")
    plt.legend()
    plt.show()
a()

def b():

    data = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos3b.dat")

    hx = data[0]
    hy = data[1]
    
    #Elimino el par cercano a cero
    hx = hx[1:]
    hy = hy[1:]
    
    x = 0
    m = len(hx)
    y = 0
    x_cuad = 0
    x_y = 0

    for i in range(0,m):
        x = x + float((1/hx[i]))
        y = y + float(1/hy[i])
        x_cuad = x_cuad + (float(1/hx[i])**2)
        x_y = x_y + float((1/hx[i])*float(1/hy[i]))

    #bx + a
    a = (((x_cuad*y)-(x_y*x))/((m*x_cuad)-(x**2)))
    b = ((m*x_y)-(x*y))/((m*x_cuad)-(x**2))
    
    fun = hx/((a*hx) + b)

    plt.plot(hx,fun,label="Aproximacion",color="blue")
    plt.scatter(hx,hy,label="Datos",color="red")
    plt.legend()
    plt.show()

b()