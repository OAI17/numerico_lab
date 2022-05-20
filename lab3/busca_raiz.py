from cProfile import label
from scipy import interpolate
from matplotlib import pyplot as plt

fig, axs = plt.subplots(layout='constrained')

def spline(fun,x0,x1,x2,err,mit):

    xn = [x0,x1,x2]
    hx = []
    hy = []


    hx_new = []
    hy_new = []

    for i in range(0,len(xn)):
        for j in range(i-2,i+1):
            hx.append(j)
            hy.append(fun(j))
          
        fun_interpol = interpolate.interp1d(hx,hy,kind="quadratic")

        n = i-2
        while (n <= i):
            hx_new.append(n)
            hy_new.append(fun_interpol(n))
            n = n + 0.1
        
        axs.plot(hx_new,hy_new,label=i)

        hx = []
        hy = []
        hx_new = []
        hy_new = []
    
    axs.legend()
    plt.show()
    
def func_ej(x):
    return (-(x**2))


#spline(func_ej,-1,0,1,0,0)

def rinterp(fun,x0,x1,x2,err,mit):
    pass