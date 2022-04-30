from math import factorial
from rbisec import rbisec
from matplotlib import pyplot as plt

def serie_seno(x):
    sumatoria = 0
    for n in range(5):
        term1 = (-1)**n
        aux = (2*n)+1
        term2 = factorial(aux)
        term3 = x**(aux)
        result = (term1*term3)/term2
        sumatoria = sumatoria + result
    return sumatoria
#para ejecutar el ej de arriab descomentar la linea de abajo(usar cualquier x, en este ejmplo uso x=3)
#serie_seno(3)


def ej3():
    print("Calculo de raices con metodo de biseccion")
    hx1, hy1 = rbisec(serie_seno,[3,4],1e-5,100)
    hx2, hy2 = rbisec(serie_seno,[4,5.5],1e-5,100)
    raiz1 = hx1[-1]
    raiz2 = hx2[-1]
    print(f"la primera riaz positiva es {raiz1}, la segunda riaz positiva es {raiz2}")
    return raiz1,raiz2 #lo hago de esta forma para poder graficar las raices en ej2
#para ejecutar el ej de arriab descomentar la linea de abajo
#ej3()

def ej2():
    x = 0
    hy = []
    hx = []
    while (x<=6.4):
        aprox = serie_seno(x)
        hy.append(aprox)
        hx.append(x)
        x = x + 0.001  
    r1,r2 = ej3()
    plt.plot(hx,hy,color="black",label="serie seno")
    plt.scatter(r1,0,color="red",label="raiz1")
    plt.scatter(r2,0,color="green",label="raiz2")
    plt.grid(True)
    plt.legend()
    plt.show()
#para ejecutar el ej de arriab descomentar la linea de abajo
#ej2()

def rrsteffensen(fun,x0,err,mit):
    hx = []
    hy = []
    
    f_xn = fun(x0)
    v = f_xn**2
    
    for x in range(mit):

        denominador = fun(x0+f_xn) - f_xn
        
        if denominador == 0:
            print("no puedo dividir por cero")
            break

        x1 = x0 -(v/denominador)
        
        f_xn = fun(x1)
        v = f_xn**2
        
        hx.append(x1)
        hy.append(v)
        
        x0 = x1

        if (abs(f_xn) < err) or (x >= mit):
            break

    return (hx,hy)
#para ejecutar el ej de arriab descomentar la linea de abajo(los parametros utilizados son solo de ej)
#rrsteffensen(serie_seno,2,1e-5,100)

def ej5():
    print("Calculo de raices con metodo de Steffensen")
    hx1,hy1 = rrsteffensen(serie_seno,3,1e-5,100)
    hx2,hy2 = rrsteffensen(serie_seno,6,1e-5,100)    
    print(f"la primera riaz positiva es {hx1[-1]}, la segunda riaz positiva es {hx2[-1]}")
    '''
    cuando inicio la busqueda en 4.5 se produce un overflow 
    la busqueda con punto inicial 3, usa las 1 iteracion
    la busqueda con punto inicial 6, usa las 69 iteraciones

    '''
#para ejecutar el ej de arriab descomentar la linea de abajo
#ej5()
