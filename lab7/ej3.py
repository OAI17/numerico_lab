from scipy.optimize import linprog
import numpy as np 
from matplotlib import pyplot as plt

costo = np.array([-25,-20])

vector = np.array([25,10])

matriz = np.array([[3,4],
                  [2,1]])

op = linprog(costo, A_ub=matriz, b_ub=vector, method='simplex')
print(f"Solucion es {-op.fun}")

x = np.linspace(0,5)
y1 = (25/4) - (3/4)*x
y2 = 10 - 2*x

plt.plot(x,y1)
plt.plot(x,y2)
plt.scatter(op.x[0],op.x[1])
plt.show()

