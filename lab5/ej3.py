from ej1 import *
import numpy as np
from matplotlib import pyplot as plt
import math
#trapecio(fun,a,b,N,error)


def senint(x,m,i):   
    sub_int = math.ceil(x/0.1)
    fun = lambda x : np.cos(x)
    hy.append(trapecio(fun,0,x,sub_int,0))
    hsen.append(np.sin(x))

hy = []
hsen = []
hx = np.linspace(0,2*np.pi,14)
m = len(hx)

for i in range(0,m):
    senint(hx[i],m,i)

plt.scatter(hx,hy,color='red')
plt.plot(hx,hsen)
plt.show()