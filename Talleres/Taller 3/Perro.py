import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def interpolación (x, y):
    n = len(x)
    R = np.zeros((n,n), float)
    B = np.copy(y)
    ult = n-1
    
    for i in range(0,n): #Matriz vandermomde
        for j in range(0,n):
            p = ult-j
            R[i,j] = x[i]**p
        
    coef = np.linalg.solve(R,B)
    
    varX = sp.Symbol("x")
    pot = 0
    polin = 0
    for i in range (0,n):
        pot = (n-1)-i
        aux = coef[i]*(varX**pot)
        polin = polin + aux

    auxX = sp.lambdify(varX, polin)
    Gx = np.linspace(np.min(x), np.max(x), 20)
    Gy = auxX(Gx)
    plt.plot(Gx,Gy, 'r-')

#CURVA 1
curva1 = np.array([(1, 3), (2.5,3.7), (5.2,4.2), (8.5, 6.5), (12.3,7.1), (15,6), (17,4.5)], float)
xi, yi = zip(*curva1)

x = np.array(xi, float)
y = np.array(yi, float)
plt.plot(x,y, 'b--')

interpolación(x,y)
p = lagrange(x,y)

print("\n->Curva 1 Superior.\nPolinomio mediante interpolacion de lagrange:\n")
print(p)


#CURVA 1 INFERIOR
curva1 = np.array([(1, 3), (2.5,2.7), (4.8,2.85), (7.5,3), (7.9,2.1)], float)
xi, yi = zip(*curva1)

x = np.array(xi, float)
y = np.array(yi, float)
plt.plot(x,y, 'b--')

interpolación(x,y)
p = lagrange(x,y)

print("\n->Curva 1 Inferior.\nPolinomio mediante interpolacion de lagrange:\n")
print(p)


#CURVA 1.2 INFERIOR
curva1 = np.array([(7.9,2.1), (10.5,2.4), (13,2), (17,2)], float)
xi, yi = zip(*curva1)

x = np.array(xi, float)
y = np.array(yi, float)
plt.plot(x,y, 'b--')

interpolación(x,y)
p = lagrange(x,y)

print("\n->Curva 1.2 Inferior.\nPolinomio mediante interpolacion de lagrange:\n")
print(p)


#CURVA 2
curva2 = [(17,4.5),(19.5,7.0), (23, 6.1), (24.5,5.4), (27,5), (27.7,4.1)]
xi, yi = zip(*curva2)

x = np.array(xi, float)
y = np.array(yi, float)
plt.plot(x,y, 'b--')

interpolación(x,y)
p = lagrange(x,y)

print("\n->Curva 2 Superior.\nPolinomio mediante interpolacion de lagrange:\n")
print(p)


#CURVA 2 INFERIOR
curva2I = np.array([(17,2), (22,1.7), (25,1.5), (28,2.6)], float)
xi2, yi2 = zip(*curva2I)

x2I = np.array(xi2, float)
y2I = np.array(yi2, float)
plt.plot(x2I,y2I, 'b--')

interpolación(x2I,y2I)
p = lagrange(x2I,y2I)

print("\n->Curva 2 Inferior.\nPolinomio mediante interpolacion de lagrange:\n")
print(p)


#CURVA 3
curva3 = [(27.7,4.1), (29,4.1), (30,3.0)]
xi, yi = zip(*curva3)

x = np.array(xi, float)
y = np.array(yi, float)
plt.plot(x,y, 'b--')

interpolación(x,y)
p = lagrange(x,y)

print("\n->Curva 3 Superior\nPolinomio mediante interpolacion de lagrange:\n")
print(p)


#CURVA 3 INFERIOR
curva2I = np.array([(28,2.6), (29,2.5), (30,3)], float)
xi3, yi3 = zip(*curva2I)

x3I = np.array(xi3, float)
y3I = np.array(yi3, float)
plt.plot(x3I,y3I, 'b--')

interpolación(x3I,y3I)
p = lagrange(x3I,y3I)

print("\n->Curva 3 Inferior\nPolinomio mediante interpolacion de lagrange:\n")
print(p)

plt.plot(19,19)
plt.plot()
plt.show()