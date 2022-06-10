from scipy.integrate import quad
import numpy as np

fun1 = lambda x : np.exp(-(x**2))

I1 = quad(fun1, -np.Inf, np.Inf)

fun2 = lambda x : (x**2)* np.log(x + (((x**2)+1))**2)

I2 = quad(fun2, 0, 2)

print(I1)
print(I2)