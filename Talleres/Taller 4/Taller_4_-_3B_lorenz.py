import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import warnings
warnings.simplefilter("ignore")


#Metodo Runge Kutta
def rungeKutta(v, lorenz):
    
    h= 0.05
    lista_t = np.arange(1,50,0.002)   
    X,Y,Z=[],[],[]
    
    def fun(v):   
        x,y,z = (v[0], v[1], v[2])
        fx, fy, fz = lorenz(x,y,z)
        return np.array([fx,fy,fz],float)
      
    for t in 100:   
        k1=h*fun(v)
        k2=h*fun(v+(0.5*k1))
        k3=h*fun(v+(0.5*k2))
        k4=h*fun(v+k3)
        
        v += (k1+2*k2+2*k3+k4)/float(6)
        
        X.append(v[0])
        Y.append(v[1])
        Z.append(v[2])
    return np.array([X,Y,Z])


#Sistema de lorenz
def lorenz(x,y,z):
    
    f1 = b*(-x+y)
    f2 = ((c*x)-y)-(x*z)
    f3 = (x*y)-(a*z)
    
    #f1 = (a*x) + (y*z)
    #f2 = b*(y-z)
    #f3 = (-x*y) + ((c*y)-z)
    return f1, f2, f3

a = 8/3
b = 10
c = 28
v=[1,1,1] #variables x,y,z

#FUNCION
x,y,z = rungeKutta(v, lorenz)

#GRAFICAR
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x,y,z)
plt.show()
