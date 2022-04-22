from puntofijo import ripf
from rbisec import rbisec
from newton import rnewton
import math
import matplotlib.pyplot as plt

x = 0
f = lambda y : y - math.exp(-((1-x*y)**2))
g = lambda y : math.exp(-((1-x*y)**2))
h = #es la funcion para newton y tiene que devolver una tupla con la funcoin y la derivada evaluada en x0
hx = []
hy_pf = []
hy_bis = []
hy_new= [] 


while(x <= 1.5):
    #Punto fijo
    conv_pf = ripf(g,0,1e-5,100) #aprox mas cercana a la raiz
    hy_pf.append(conv_pf[-1])
    
    #Punto bisec
    conv_bis = rbisec(f,[0,1.5],1e-5,100)
    hy_bis.append(conv_bis[0][-1]) 
    
    #Newton
    conv_new = rnewton(f,0,1e-5,100)
    hy_new.append(conv_new[0][-1])

    hx.append(x)
    x = x + 0.005


plt.plot(hx,hy_new)
plt.show()


