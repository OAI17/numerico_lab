from dis import dis
import numpy as np 
from matplotlib import pyplot as plt 

def a():
    hy = []
    dist = np.linspace(0,1,50)

    for i in range(0,len(dist)):
        evaluate = np.arcsin(dist[i])
        hy.append(evaluate)

    for j in range(0,5):
        hy_poly = []
        
        coef = np.polyfit(dist,hy,j)
        
        for k in range(0,len(dist)):
            hy_poly.append(np.polyval(coef,dist[k]))
        
        g = f"Pol de grado {j}"
        plt.plot(dist,hy_poly,label=g)
    plt.legend()
    plt.show()

a() 
def b():
    hy = []
    dist = np.linspace(0,(4*np.pi),50)
    hy_cos = []
    for i in range(0,len(dist)):
        evaluate = np.cos(dist[i])
        hy.append(evaluate)
        hy_cos.append(evaluate)

    for j in range(0,5):
        hy_poly = []
        
        coef = np.polyfit(dist,hy,j)
        
        for k in range(0,len(dist)):
            hy_poly.append(np.polyval(coef,dist[k]))
        
        g = f"Pol de grado {j}"
        plt.plot(dist,hy_poly,label=g)
    plt.plot(dist,hy_cos,label="cos")
    plt.legend()
    plt.show()

b()

"Este tipo de aprox no funciona muy bin para funciones trigonometricas"