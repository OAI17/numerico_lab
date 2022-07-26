from matplotlib import pyplot as plt
import numpy as np

from rbisec import rbisec
xs = np.linspace(1/2,(np.pi/2)-(1/2),100) #esta es una aprox, puedo notar que cambia de signo en dicho intervalo entonces es conviente usar biseccion
f = (1/xs) - np.tan(xs)

fun = lambda x :(1/x) - np.tan(x)
solx, soly = rbisec(fun,(1/2,(np.pi/2)-(1/2)),-100e1000,1000)
print(solx[-1],soly[-1])
plt.scatter(solx[-1],soly[-1],label="Raiz")
plt.plot(xs,f)
plt.legend()
plt.show()