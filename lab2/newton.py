import math
import matplotlib.pyplot as plt
#{pre de fun: deveulva una tupla con f,f' evaluda en x }
def rnewton(fun,x0,err,mit):
    hx = []
    hy = []
    
    v, dv = fun(x0) #devuele f y f' en x0 en forma de tupla
     
    for x in range(1,mit):
        if abs(dv) == 0:
            print("no puedo dividir por cero")
            break

        x1 = x0 -(v/dv)
        v, dv = fun(x1)
        
        hx.append(x1)
        hy.append(v)
        
        print(f"iteracion {x}, aprox {x1}")

        if abs(x1-x0) < err:
            break

        x0 = x1

    return (hx,hy)


def riaz_cubica(x):
    #print("aproximar raiz cubica de a con x**3 -a = 0")
    fun_s = (x**3)-2
    fun_der = (3)*(x**2)
    return (fun_s,fun_der)
#rnewton(riaz_cubica,3,10e-6,100)
