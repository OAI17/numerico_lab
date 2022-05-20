from dis import dis
import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos1a.dat")


hx = data[:,0] #todos las datos de la columna cero(primera columna)
hy = data[:,1]

def dif_divididas():
    m = len(data)
    x = 0
    y = 0
    x_cuad = 0
    x_y = 0


    for i in range(0,m):
        x = x + float(hx[i])
        y = y + float(hy[i])
        x_cuad = x_cuad + (float(hx[i])**2)
        x_y = x_y + float((hx[i])*float(hy[i]))

    # ax + b
    a = ((m*x_y)-(x*y))/((m*x_cuad)-(x**2))
    b = ((x_cuad*y)-(x_y*x))/((m*x_cuad)-(x**2))


    hx_new = []
    hy_new = []


    for k in range(0,m):
        fun = (a*hx[k]) + b
        #hx_new.append(k)
        hy_new.append(fun)


    plt.plot(hx,hy_new)
    plt.scatter(hx,hy)
    plt.show()


def np_div():
    m = len(data)
    ones = np.ones(m)
    x = np.dot(ones,hx)
    y = np.dot(ones,hy)
    x_cuad = np.dot(hx,hx)
    x_y = np.dot(hx,hy)

    
    # ax + b
    a = ((m*x_y)-(x*y))/((m*x_cuad)-(x**2))
    b = ((x_cuad*y)-(x_y*x))/((m*x_cuad)-(x**2))


    hx_new = []
    hy_new = []


    for k in range(0,m):
        fun = (a*hx[k]) + b
        #hx_new.append(k)
        hy_new.append(fun)


    plt.plot(hx,hy_new)
    plt.scatter(hx,hy)
    plt.show()

def np_all():
    hy = []
    hy_f = []
    hy_poly = []

    polinomio = [3/4,-1/2]
    fun = lambda x : ((3/4)*x)-1/2

    dist = np.linspace(0,10,20)
    distY = np.random.randn(20)


    for i in range(0,len(dist)):
        x = dist[i]
        evalute = np.polyval(polinomio,x) + distY[i]  
        hy.append(evalute)
        hy_f.append(fun(x))


    coef = np.polyfit(dist,hy,1)

    for j in range(0,len(dist)):
        x = dist[j]
        hy_poly.append(np.polyval(coef,x))    
     

    plt.scatter(dist,hy)
    plt.plot(dist,hy_f)
    plt.plot(dist,hy_poly)
    plt.legend()
    plt.show()
np_all()