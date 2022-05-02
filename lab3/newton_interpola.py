import numpy as np 

def dif_div(xi,yi):
    n = len(xi)
    m = len(yi)

    ci = np.zeros((n,m))

    coeficientes = []
    coeficientes.append(yi[0])

    for h in range(m):
        ci[h][0] = yi[h]
        

    for j in range(1,m):
        for i in range(0,m-j):
            calc = ((ci[i+1][j-1])-(ci[i][j-1]))/((xi[j+i])-xi[i])
            ci[i][j] = calc
            
        coeficientes.append(ci[0][j])
    
    return coeficientes


def calculate_produc(mit,pto,xs):
    produc = 1

    if mit > 0:
        for j in range(0,mit):
            produc = produc * (pto-xs[j])
        return produc
    else:
        return 1


def inewton(x,y,z):
    ci = dif_div(x,y)
    evaluate = []
    for k in range(len(z)):
        sumatoria = 0
        for i in range(len(ci)):
            produc = calculate_produc(i,z[k],x)
            sumatoria = sumatoria + (ci[i]*produc)
        evaluate.append(sumatoria)
    return evaluate


print(inewton([2, 2.5 , 4],[0.5 , 0.4 , 0.25],[1,2,3]))
