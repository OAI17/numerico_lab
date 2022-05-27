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
        x = x + float(np.log(hx[i]))
        y = y + float(np.log(hy[i]))
        x_cuad = x_cuad + (float(hx[i])**2)
        x_y = x_y + float((hx[i])*float(hy[i]))

    # ax + b
    a = ((m*x_y)-(x*y))/((m*x_cuad)-(x**2))
    b = np.log(((x_cuad*y)-(x_y*x))/((m*x_cuad)-(x**2)))


    hx_new = []
    hy_new = []


    for k in range(0,m):
        fun = (a*hx[k]) + b
        hy_new.append(fun)


    plt.plot(hx,hy_new,label="Aproximacion",color="blue")
    plt.scatter(hx,hy,label="Datos",color="red")
    plt.legend()
    plt.show()


def b():

    data = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos3b.dat")

    hx = data[0]
    hy = data[1]


    m = len(hx)
    x = 0
    y = 0
    x_cuad = 0
    x_y = 0
    
    for i in range(0,m):
        x = x + float((hx[i]))
        y = y + float((hy[i]))
        x_cuad = x_cuad + (float(hx[i])**2)
        x_y = x_y + float((hx[i])*float(hy[i]))

    # ax + b
    a = ((m*x_y)-(x*y))/((m*x_cuad)-(x**2))
    b = ((x_cuad*y)-(x_y*x))/((m*x_cuad)-(x**2))

    hy_new = []

    for k in range(0,m):
        fun = (a*hx[k] + b)
        hy_new.append(fun)


    plt.plot(hx,hy_new,label="Aproximacion",color="blue")
    plt.scatter(hx,hy,label="Datos",color="red")
    plt.legend()
    plt.show()
b()