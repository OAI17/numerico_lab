import math
import matplotlib.pyplot as plt

def rnewton(fun,x0,err,mit):
    hx = []
    hy = []
    #a = int(input("Ingrese un valor: "))
    #fun_xn = fun(x0)
    fun_xn = fun(x0)    
    fun = fun_xn[0]
    derivade_fun = fun_xn[1]

    v = fun_xn[0]

    for k in range(1,mit):
        x1 = x0 -v/fun_xn[1]
        fun_xn = fun(x1,a)
        v = fun_xn[0]
        hx.append(x1)
        hy.append(v)
        print(f"iteraciones {k},aproximacion {x1}, error {v}")#no estoy seguro de que v sea el error
        if abs(v) < err:
            break
        x0 = x1 
    return (hx,hy)


def fun(x,a):
    #aproximar raiz cubica de a con x**3 − a = 0
    fun_s = (x**3)-a
    fun_der = (3)*(x**2)
    return (fun_s,fun_der)
#rnewton(fun,10,10e-6,100)




