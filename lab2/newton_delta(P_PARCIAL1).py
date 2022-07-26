import math
import matplotlib.pyplot as plt
from newton import rnewton
#{pre de fun: deveulva una tupla con f,f' evaluda en x }
def rnewtondelta(fun,x0,err,mit,delta):
    hx = []
    hy = []
    v = fun(x0) #devuele f 
    
    if delta == 0:
        print("no puedo dividir por cero")
        exit()
    
    dv = (fun(x0+delta)-v)/delta
    
    for x in range(1,mit+1):
        if abs(dv) == 0:
            print("no puedo dividir por cero")
            break

        x1 = x0 -(v/dv)
        v = fun(x1)
        dv = (fun(x1+delta)-v)/delta
        hx.append(x1)
        hy.append(v)
        
        #print(f"iteracion {x}, aprox {x1}")

        if (abs((x1-x0)/x1) < err) or (abs(v) < err):
            print(f"cantidad de iteraciones newton_delta {x}")        
            return (hx,hy)
            
        x0 = x1
    print(f"cantidad de iteraciones newton_delta {mit}")
    return (hx,hy)



from matplotlib import pyplot as plt
import numpy as np

def fun(x):
    f = ((np.e)**x)-x-2
    return f

def fun2(x):
    f = ((np.e)**x)-x-2
    f_d = (np.e)**x -1
    return (f,f_d)

rnewton(fun2,1,1e-6,100)

xs = np.linspace(0,10, num=300)
f = ((np.e)**xs)-xs-2
plt.plot(xs,f)
xn, yn = rnewtondelta(fun,1,1e-6,100,1e-5)
plt.scatter(xn[-1],yn[-1],label=f"{xn[-1],yn[-1]}")
plt.legend()
plt.show()

