from scipy.optimize import linprog
import numpy as np 
from matplotlib import pyplot as plt

costo = np.array([-7,-4,-3])

vector = np.array([30,45])

matriz = np.array([[1,2,2],
                   [2,1,2]])


op = linprog(costo, A_ub=matriz, b_ub=vector, method='simplex')
print(f"Va a fabricar {op.x[0]} rubia, {op.x[1]} negra y {op.x[2]} baja")
print(f"La cantidad de plata ganada {-op.fun}")