from puntofijo import ripf
from rbisec import rbisec
from newton import rnewton
import math
import matplotlib.pyplot as plt


def newton_functions(x0):
    x=0
    f = lambda y : y - math.exp(-((1-x*y)**2))
    fun_der = lambda y : y - math.exp(-1+(2*y)-(y**2))
    fun_s = f(x0)
    fun_der_ev = fun_der(x0)
    return (fun_s,fun_der_ev)


x = 0
f = lambda y : y - math.exp(-((1-x*y)**2))
g = lambda y : math.exp(-((1-x*y)**2))
h = newton_functions
hx = []
hy_pf = []
hy_bis = []
hy_new= [] 

#conv_new = rnewton(newton_functions,0,1e-5,100)

while(x <= 1.5):
    #Punto fijo
    conv_pf = ripf(g,0,1e-5,100) #aprox mas cercana a la raiz
    hy_pf.append(conv_pf[-1])
    
    #Punto bisec
    conv_bis = rbisec(f,[0,1.5],1e-5,100)
    hy_bis.append(conv_bis[0][-1]) 
    
    #Newton
    #conv_new = rnewton(h,0,1e-5,100)
    #hy_new.append(conv_new[0][-1])

    hx.append(x)
    x = x + 0.005

fig, axs = plt.subplots(2)
fig.suptitle("Compraracion metodos de iteracion")
axs[0].plot(hx,hy_bis)
axs[0].set_title("Metodo de bisceccion")
axs[1].plot(hx,hy_pf)
axs[1].set_title("Metodo de punto fijo")
#axs[2].plot(hx,hy_new)
#axs[2].set_title("Metodo de newton")
plt.show()



