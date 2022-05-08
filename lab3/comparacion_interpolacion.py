from matplotlib import pyplot as plt 
from newton_interpola import inewton

hx =[]
hy1 = []
hy2 = []
hz = []

func = lambda x : 1/(1+25*(x**2))
dist = lambda j : (-2/200)+(j/200)

i = 10

for j in range(1,200):
    hz.append(dist(j))

    if j <= i:
        hy1.append(func(j))
        hx.append(j)




hw = inewton(hx,hy1,hz)


fig, axs = plt.subplots(layout='constrained')
axs.plot(hz,hw,label="a")
axs.plot(hx,hy1,label="b")
axs.legend()
plt.show()



