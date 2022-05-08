from dis import dis
from newton_interpola import inewton
from matplotlib import pyplot as plt

func = lambda x : 1/x
dist = lambda j : ((24/25)+(j/25))


hx = []
hy = []
 

for i in range(1,101):
    hx.append(dist(i))
    hy.append(func(hx[i-1]))


hw = inewton([1,2,3,4,5],[1, 1/2, 1/3, 1/4 , 1/5 ],hx)

fig, axs = plt.subplots(layout='constrained')
axs.plot(hx,hw,label="Interpolacion")
axs.plot(hx,hy, label="Funcion")
axs.legend()
plt.show()