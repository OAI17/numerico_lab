from matplotlib import pyplot as plt
from larange_interpola import ilagrange
from newton_interpola import inewton
from scipy import interpolate

hx = [-3,-2,-1,0,1,2,3]
hy = [1,2,5,10,5,2,1]
hz = []

h_scipy_cubic = interpolate.interp1d(hx,hy,kind="cubic")
hy_scipy_cubic= []

h_scipy_linear = interpolate.interp1d(hx,hy,kind="linear")
hy_scipy_linear= []


#calculate range of graphic
j = -3
while(j<= 3):
    hz.append(j)
    hy_scipy_cubic.append(h_scipy_cubic(j))
    hy_scipy_linear.append(h_scipy_linear(j))
    j = j + 0.1

h_newton = inewton(hx,hy,hz)
h_larange = ilagrange(hx,hy,hz)

"----------------------------------------------------------------"







"----------------------------------------------------------------"
fig, axs = plt.subplots(layout='constrained')
axs.plot(hz,h_newton,label="Newton")
axs.plot(hz,h_larange,label="Larange")
axs.plot(hz,hy_scipy_cubic,label="Scipy Cubico")
axs.plot(hz,hy_scipy_linear,label="Scipy Lineal")
axs.legend()
plt.show()

'''
Podemos notar que el scipy cubico es el polinomio mas suave,
seguido de larange y newton que aproximan edenticamente 
y por ultimo el scipy lineal que no es para nada suave
'''


