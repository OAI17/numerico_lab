def calculate_li(indice_sum,list_x,pto):
    value = 1
    for j in range(len(list_x)):
        if indice_sum != j:
            xj = list_x[j]
            xi = list_x[indice_sum]
            value = value * ((pto-xj)/(xi-xj))
    return value

def calculate_sumatoria(x,y,pto):
    sumatoria = 0
    for i in range(len(x)):
        sumatoria= sumatoria + calculate_li(i,x,pto) * y[i]
    return sumatoria

def ilagrange(x,y,z):
    evaluate = []   
    for l in range(len(z)):
        evaluate.append(calculate_sumatoria(x,y,z[l]))
    return evaluate




print(ilagrange([2, 2.5 , 4],[0.5 , 0.4 , 0.25],[1,2,3]))