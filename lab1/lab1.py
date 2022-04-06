#https://github.com/lbiedma/anfamaf2022
import math 
import random

#ej1
def ej1():
    x = int(input("Ingrese un valor para la variable x: "))
    y = int(input("Ingrese un valor para la variable y: "))
    z = int(input("Ingrese un valor para la variable z: "))

    r1 = x/y+z
    r2 = x/(y+z)
    r3 = x/y*z
    r4 = x/(y*z)

    print(f"Resultado de la expresion x/y+z = {r1}")
    print(f"Resultado de la expresion x/(y+z) = {r2}")
    print(f"Resultado de la expresion x/y*z = {r3}")
    print(f"Resultado de la expresion x/(y*z) = 1{r4}")

#ej2
def ej2():
    a = 1 + 2**-53
    b = a-1

    if a == b:
        print(f"{a} y {b} son iguales")
    else:
        print(f"{a} y {b} son diferentes")

    c = 1 + 2**-52
    d = c-1 

    if c == d:
        print(f"{c} y {d} son iguales")
    else:
        print(f"{c} y {d} son diferentes")

#ej3
def ej3():
    base = 2 
    exponente = 1
    while exponente < 5:
        potencia = (base ** exponente)
        print(potencia)
        try:
            math.isinf(potencia)
        except:
            print("Overflow")
            break
        exponente = exponente + 1

def ej4():
    x = 0.5 #0.1
    while x != 10:
        x = x + 0.5     
        print(x)
    #Lo que pasa es que cuando va sumando de a 0.5 el valor en un mmento llega a 10 y se corta por la conhdicion del if, 
    #pero cuando suma de 0.1 nunca lelga a ser 10 excato y por lo tanto nunca corta y sigue sumando hasta el infinito

def ej5(): 
    n = 6 
    i = n
    resp = 1
    while i != 0:
        resp = resp * i
        i = i-1
    print(f"El valor de 6! es = {resp}")

    resp2 = math.factorial(n)
    print(f"El valor de 6! usando math es = {resp2}")

def ej5_c(n):
    i = n
    resp = 1 
    if n == 0:
        print(f"El valor de {n}! es = {resp}")
    else:
        while i != 0:
            resp = resp * i
            i = i -1
        print(f"El valor de {n}! es = {resp}")

#ej6
def ej6(n1,n2):
    if n1 > n2:
        print(f"{n1} es mayor que {n2}")
    
    elif n2 > n1:
        print(f"{n2} es mayor que {n1}")    
    
    else:
        print(f"{n1} es igual que {n2}")

#ej7
def ej7(x,n):
    resp = 1
    i = n
    while i != 0: 
        resp = resp * x
        i = i -1
        if i > abs(n-5):
            print(resp)
    print(resp)

#ej8 
def mala(a,b,c):
    discriminante = ((b*2)-(4*a*c)) * 0.5
    if discriminante < 0:
        print("Discriminante menor a 0 intente de nuevo")
        return None
    resp1 = (-b + discriminante)/2*a
    resp2 = (-b - discriminante)/2*a    
    return [resp1,resp2]
    print(f"x1 = {resp1} y x2 = {resp2}")

def buena(a,b,c):
    discriminante = ((b*2)-(4*a*c)) * 0.5
    resp1 = (-b + discriminante)/2*a
    resp2 = (-resp1) -(b/a) 
    return [resp1,resp2]
    print(f"x1 = {resp1} y x2 = {resp2}")

#ej9 
def horn(coef,x):
    n = len(coef)
    b = coef[0]
    for i in range(1,n):
        b = coef[i] + x * b 
    return b 

#ej10
def sonReciprocos(x,y):
    if x*y == 1:
        #print(f"{x} y {y} son reciprocos")
        return True
    else:
        return False
      
def ej10():
    for i in range(100):
        x = 1 + random.random()
        y = 1/x
        if not(sonReciprocos(x,y)):
            print(x)

#devuelve todos los random x que no son reciprocos 

#ej11
def func(x):
    a = (((x**2)+1)**0.5)-1
    b = ((x**2))/((((x**2)+1)**0.5)+1)
    return (a,b)

def ej11(x):
    for i in range(20):
        x = 8**-i
        resp = func(x)
        print(f"f(x)={resp[0]}, g(x)={resp[1]}")
#las dos funciones lo mismo hasta un cierto punto despues la funcion g(x) tiene mayor presicion 

#ej12
def sonOrtogonales(vec_x,vec_y):
    calc = (vec_x[0]*vec_y[0]) + (vec_x[1]*vec_y[1])
    if calc == 0:
        return True
    
def ej12():
    x = [1,1.1024074512658109]
    y = [-1, 1/x[1]]

    if not sonOrtogonales(x,y):
        print("Algo salio mal")

#posiblemente lo que pase es que la computadora no tiene la precicion necesaria o tine mucha precicion y le erra por poco 

