from scipy.optimize import linprog
import numpy as np 
from matplotlib import pyplot as plt

matriz = np.array([[-3,-2],
                  [-1,-3],
                  [-8,-2]])

vector = np.array([-3,-1.5,-4])

costo = np.array([10, 8])

op = linprog(costo, A_ub=matriz, b_ub=vector, method='simplex')
resp = op.x
print(f"Cuesta {op.fun}")


x = np.linspace(0,1)
y1 = (3/2) - (3/2)*x
y2 = (1/2) - (1/3)*x
y3 = 2 - 4*x
y4 = np.maximum(y1, np.maximum(y2,y3))


plt.scatter(resp[0],resp[1])
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.fill_between(x,2.5,y4)
plt.show()