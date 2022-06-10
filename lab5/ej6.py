from scipy.integrate import quad
import numpy as np

def nat_to_rad(a):

    return np.radians(a)

def calculate_integral(tita):
    fun = lambda x : (1/((1 - ((np.sin(tita/2)**2) * (np.sin(x)**2))) ** (1/2)))
    a = 0
    b = np.pi / 2
    result = quad(fun,a,b)
    return result

def calculate_rest(l):
    g = 9.8
    return 4 * ((l/g)**(1/2))


degree = int(input("Ingrese un grado entre 0 y 90: "))
longitud = int(input("Ingrese una longitud: "))

rest = calculate_rest(longitud)
radianes = nat_to_rad(degree)
I = calculate_integral(radianes)

result = I[0] * rest

print(result)

