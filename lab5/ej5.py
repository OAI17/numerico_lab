from scipy.integrate import quad
import numpy as np

fun = lambda x : np.exp(-(x**2))

I = quad(fun, -np.Inf, np.Inf)

print(I)