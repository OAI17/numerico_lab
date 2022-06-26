from scipy.optimize import linprog
import numpy as np 
from matplotlib import pyplot as plt



vector1 = np.array([200,300,245,190])
vector2 = np.array([-1, -1, -1, -1])

costo_base = np.array([68.3, 69.5, 71, 71.2])
costo = vector1 * costo_base

matriz1 = np.array([[52, 212, 25, 60],
                   [57, 218, 23, 57],
                   [51, 201, 26, 54],
                   [56, 223, 21, 55]])

matriz2 = np.array([[-52, -57, -51, -56],
                    [-212, -218, -201, -223],
                    [-25, -23, -26, -21],
                    [-60, -57, -54, -55]])


op = linprog(costo, A_eq=matriz1, b_eq=vector1, A_ub=matriz2, b_ub=vector2)

print("Solucion:")

for i in range(0, len(op.x)):
    print(f"La cantidad de horas para el equipo {i+1} es {op.x[i]}")

print(f"La cantiad de dinero que costara es de {op.fun}")
