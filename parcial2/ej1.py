import numpy as np 
from matplotlib import pyplot as plt
from aux import ilagrange
from scipy.interpolate import interp1d

data = np.loadtxt("irma.csv", dtype=float, delimiter=",")

data_hora = data[:,0]
data_long = data[:,1]
data_lati = data[:,2]

#ej1
def grafico():
    print("El grafico del punto a: ")
    plt.scatter(data_long,data_lati)
    plt.title("Datos")
    plt.ylabel("Latitud")
    plt.xlabel("Longitud")
    plt.show()

#ej2
def org_datos():
    longitud = lambda t : data_long[t]
    latitud = lambda t : data_lati[t]


    hx_n = []
    hylon = []
    hylat = []

    #obtengo los ptos que voy a interpolar
    for i in range(0,len(data_hora)): 
        hx_n.append(data_hora[i])
        hylat.append(latitud(i))
        hylon.append(longitud(i))

    return hx_n,hylon,hylat

#calculo interpolacion con larange
def larange_lati_long(horas,x,y_lati,y_long):
    # (x_,y_) son los puntos a interpolar
    ptos_lati = ilagrange(x,y_lati,horas) 
    ptos_long = ilagrange(x,y_long,horas)
    return ptos_lati,ptos_long

#calculo interpolacion con spline
def spline_lati_long(horas,x,y_lati,y_long):
    f_interpol_lati = interp1d(x,y_lati,kind='cubic') 
    f_interpol_long = interp1d(x,y_long,kind='cubic')
    ptos_lati = f_interpol_lati(horas)
    ptos_long = f_interpol_long(horas)
    return ptos_lati,ptos_long

#grafico
def grafico_ojoH():
    print("El grafico del punto b: ")
    hx_n, hylon, hylat = org_datos() #ejex, ejy long, ejy lati 
    horas = np.linspace(0,24,25) # los puntos a evaluar
    lati_interpolL,long_interpolL = larange_lati_long(horas,hx_n,hylat,hylon)
    lati_interpolS,long_interpolS = spline_lati_long(horas,hx_n,hylat,hylon)

    plt.plot(long_interpolL,lati_interpolL,label="Larange",color="red")
    plt.plot(long_interpolS,lati_interpolS,label="Spline",color="purple")

    plt.scatter(hylon,hylat,label="Datos")
    plt.title("Ojo del huracan")
    plt.ylabel("Latitud")
    plt.xlabel("Longitud")
    plt.legend()
    plt.show()


grafico()
grafico_ojoH()

