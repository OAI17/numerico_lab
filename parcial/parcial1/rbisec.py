import math 
import matplotlib.pyplot as plt

def rbisec(fun,I,err,mit):
    hx = []
    hy = []
    u = fun(I[0])
    v = fun(I[1])
    e = I[1]-I[0]
    if math.copysign(u,v) == u:
        print("Stop")
    
    else:
        for k in range(1,mit):
            e = e/2
            c = I[0] + e
            w = fun(c)
            hx.append(c)
            hy.append(w)
            if abs(e) < err:
                break

            if math.copysign(w,u) == w:
                I[0] = c
                u = w
            else:
                I[1] = c
                v = w
    return (hx,hy)



