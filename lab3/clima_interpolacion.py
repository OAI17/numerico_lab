from cmath import isnan
from telnetlib import STATUS
import numpy as np 
from matplotlib import pyplot as plt
from scipy import interpolate 


data = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos_aeroCBA.dat",dtype=str)
#data = np.where(data_nan=='NaN', '0', data_nan)

hx = []
hy = []


for j in range(len(data)): 
    temporal = float(data[j][1])
    status = np.isnan(temporal)
    if (not status):
        hx.append(int(data[j][0]))
        hy.append(temporal)
    #print(f"{data[j][0]} año,  temp {data[j][1]}")

f = interpolate.interp1d(hx,hy,kind="cubic",fill_value="extrapolate")

hw = []
hx_new = []

for j in range(1957,2017): 
    hx_new.append(j)
    hw.append(f(j))

plt.plot(hx_new,hw)
plt.xlabel("años")
plt.ylabel("temp")
plt.legend()
plt.show()

