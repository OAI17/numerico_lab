def ripf(fun,x0,err,mit):
    hx = []
    i = 0

    while (i <= mit):
        
        x = fun(x0)
        print(f"iteraciones {i} aprox {x}")

        if (abs(x-x0) < err) or (i >= mit):
            break

        hx.append(x)
        
        i = i+1
        x0 = x 
    
    return hx

def fun_lab2ej6(x):
    valor = 2**(x-1)
    return valor
    
x0 = -1
hx = ripf(fun_lab2ej6, x0, 1e-5, 100)
'''
x0=0 --> 1
x0=1,5 --> 1
x0=2,5 --> inf
x0=-1 --> 1
'''
