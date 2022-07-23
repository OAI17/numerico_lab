import math #math.copysign(a,b) devuelve el valor abs de a pero con el signo de b 
import matplotlib.pyplot as plt

def rbisec(fun,I,err,mit):
    #err es la tolerancia deseada del error
    #I= [a, b]
    #fun funcion
    #mit es el número máximo de iteraciones permitidas
    #hx= [] es una lista que representa el historial de puntos medios x
    #hf= [] el historial de los respectivos valores funcionales. y 
    hx = []
    hy = []
    u = fun(I[0]) #f(a)
    v = fun(I[1]) #f(b)
    e = I[1]-I[0] #c
    #mismo signo
    if math.copysign(u,v) == u:
        print("Stop")
    #
    else:
        for k in range(1,mit):
            e = e/2
            c = I[0] + e
            w = fun(c)
            #print(f"Iteraciones {k},punto medio {c},funcion en c {w}, {e}")
            hx.append(c)
            hy.append(w)
            if abs(e) < err:
                break
        
            if math.copysign(w,u) == w:
                I[0] = c
                u = w
            else:
                I[1] = c
                v = w
    return (hx,hy)

def fun_lab2ej2a(x):
    valor = math.tan(x)-(2*x)
    return valor

def fun_lab2ej2b(x):
    valor = (x**2)-3
    return valor 

#hx,hy = rbisec(fun_lab2ej2a,[0.8, 1.4],1e-5, 100)
#hx,hy = rbisec(fun_lab2ej2b,[1, 4],1e-5, 100)
 
def grafica_a():
    x =range(-1,2)
    plt.plot(x, [fun_lab2ej2a(i) for i in x])
    plt.plot([-1,2],[0,0])
    #plt.axis([xmin,xmax,ymin,ymax]) escala de x e y 
    #plt.grid(True) te hace cuadro
    plt.show()

def grafica_b():
    x =range(0,5)
    plt.plot(x, [fun_lab2ej2b(i) for i in x])
    plt.show()
#grafica_b()
#grafica_a()

