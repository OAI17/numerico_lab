from scipy.optimize import linprog
import numpy as np 
from matplotlib import pyplot as plt

costo = np.array([-1,-1])

matriz = np.array([[50,24],
                  [30,33]])

vector = np.array([2400,2100])

op = linprog(costo, A_ub=matriz, b_ub=vector, method='simplex')
print(f"Costo es {-op.fun}")

x = np.linspace(0,70) #el max valor posible 
y = np.linspace(-70,70) 
y1 = (2400/24) - (50/24)*x
y2 = (2100/33) - (30/33)*x
y3 = np.minimum(y1,y2)

# creamos la mesh donde evaluar la función
xmesh, ymesh = np.meshgrid(x,y)
z = xmesh + ymesh

fig, ax = plt.subplots(figsize=(16,16))
ax.set_aspect('equal')
curvas = ax.contour(xmesh,ymesh,z,levels=np.linspace(.0, 100, 30))
fig.colorbar(curvas, ax=ax)
plt.fill_between(x,y3)

plt.scatter(op.x[0],op.x[1])
plt.show()

