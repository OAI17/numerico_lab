import numpy as np 

def simpson_simple(fun,a,b):
    h = (b-a)/2
    result = (h/3) * (fun(a) + (4*fun((a+b)/2)) + fun(b))
    return result

def calculate_s(fun,a,b,c):

    sAb = simpson_simple(fun,a,b)

    sAc = simpson_simple(fun,a,c)

    sCb = simpson_simple(fun,c,b)

    error = abs(sAb - sAc - sCb)
    
    return  sAb,sAc,sCb,error   


def calculate_integral(f,e,a,b):

    c = (a+b)/2

    I = calculate_s(f,a,b,c)

    q = I[0]
    q1 = I[1]
    q2 = I[2]
    error = I[3]
    if error < (15*e):
        return q1 + q2

    else:
        q += calculate_integral(f,e/2,a,c)
        q += calculate_integral(f,e/2,b,c)

    return q


f = lambda x : x * np.exp(-(x**2))
a = 0 
b = 1

print(calculate_integral(f,10e-5,a,b))

    