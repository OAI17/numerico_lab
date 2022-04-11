def ripf(fun,x0,err,mit):
    hx = []
    i = 1

    while (i <= mit):
        
        x = fun(x0)
        print(i,x)

        if (abs(x-x0) < err) or (i >= mit):
            break

        hx.append(x)
        
        i = i+1
        x0 = x 
    
    return hx

def fun_lab2ej6(x):
    valor = ((2**x)/2)-x
    return valor
    
x0 = 2
hx = ripf(fun_lab2ej6, x0, 1e-5, 100)
print(hx)
'''
ej7 usar lambda 
f = lambda x: g(x,y)
va por aca 
def funciones(y):
    for x in range(1,10):
        result = formula
        hx.append(x)
        hy.append(result)
'''