from matplotlib import pyplot as plt

hx = [0, 1.5, 2, 2.9, 4, 5.6, 6, 7.1, 8.05, 9.2, 10, 11.3, 12]
hy = [0.1, 0.2, 1, 0.56, 1.5, 2.0, 2.3, 1.3, 0.8, 0.6, 0.4, 0.3, 0.2]

def grafico():
    print("El grafico del punto a: ")
    plt.fill_between(hx,hy,label="Area del terreno")
    plt.legend()
    plt.show()


def trapecio(a,b,fA,fB):
    h = b-a
    integral = (h/2) * (fA + fB)
    return integral

def trapecio_adaptativo():
    aprox = 0
    for i in range(0,len(hx)-1):
        aprox = aprox + trapecio(hx[i],hx[i+1],hy[i], hy[i+1])
    return aprox

def metros_cubico(area):
    metros_c = area * 10
    return metros_c



integral = trapecio_adaptativo()
print(f"La aprox de la integral es {integral}")

m_c = metros_cubico(integral)
print(f"La cantidad aprox de metros cubicos de tierra que deben ser removidos es {m_c}")
    
grafico()
