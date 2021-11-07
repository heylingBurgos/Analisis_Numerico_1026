# Modelo predador-presa de Lotka-Volterra
# Sistemas EDO con Euler mejorado
import numpy as np
import matplotlib.pyplot as plt


def Euler(f,g,t0,x0,y0,h,n):
    valores = np.zeros(shape=(n+1,3),dtype=float)
    valores[0] = [t0,x0,y0]
    ti = t0
    xi = x0
    yi = y0
    for i in range(1,n+1,1):
        K1x = h * f(ti,xi,yi)
        K1y = h * g(ti,xi,yi)
        
        K2x = h * f(ti+h, xi + K1x, yi+K1y)
        K2y = h * g(ti+h, xi + K1x, yi+K1y)
        xi = xi + (1/2)*(K1x+K2x)
        yi = yi + (1/2)*(K1y+K2y)
        ti = ti + h
        
        valores[i] = [ti,round(xi,1),round(yi,1)]
    valores = np.array(valores)
    return(valores)

# Parámetros de las ecuaciones
a = 0.4
b = 0.018
c = 0.8
d = 0.023

# Ecuaciones
f = lambda t,x,y : a*x -b*x*y
g = lambda t,x,y : -c*y + d*x*y

# Condiciones iniciales
t0 = 0
x0 = 30
y0 = 4

# parámetros del algoritmo
h = 1
n = 20

# PROCEDIMIENTO
valores = Euler(f,g,t0,x0,y0,h,n)
ti = valores[:,0]

xi = valores[:,1]

yi = valores[:,2]
for i in range(len(ti)):
    ti[i]+=1900.0
    

# SALIDA en pantalla
print("SOLUCIÓN NUMERICA POR AÑOS")
print(' [ años, conejos, linces]')
print(valores)


#Datos reales
conejos = [30., 47.2, 70.2, 77.4, 36.3, 20.6, 18.1, 21.4, 22., 25.4, 27.1, 40.3, 57., 76.6, 52.3, 19.5, 11.2, 7.6, 14.6, 16.2, 24.7]
linces = [4., 6.1, 9.8, 35.2, 59.4, 41.7, 19., 13., 8.3, 9.1, 7.4, 8., 12.3, 19.5, 45.7, 51.1, 29.7, 15.8, 9.7, 10.1, 8.6]
maximoC = -1
maximoL = -1
promedioC = 0
promedioL = 0
diaC = 0
diaL = 0

print("ERRORES LOCALES")

for i in range(len(conejos)):
    errLocalC = round(abs(conejos[i]-xi[i]),1)
    errLocalL = round(abs(linces[i]-yi[i]),1)
    promedioC += errLocalC
    promedioL += errLocalL
    print("Año: {} Error Conejos: {}, Error linces: {}".format(ti[i], errLocalC, errLocalL))
    if errLocalC>maximoC:
        maximoC=errLocalC
        diaC = ti[i]
    if errLocalL>maximoL:
        maximoL=errLocalL
        diaL = ti[i]

print("ERROR PROMEDIO")
print("Conejos: {} Linces: {}".format(promedioC/len(conejos), promedioL/len(linces)))
print("ERROR MAXIMO")
print("Conejos: {} año: {}".format(maximoC, diaC))
print("Linces: {} año: {}".format(maximoL, diaL))


#grafica conejos y linces contra el tiempo
plt.plot(ti,xi, label='xi presa')
plt.plot(ti,yi, label='yi predador')

plt.title('Modelo predador-presa')
plt.xlabel('t tiempo')
plt.ylabel('población')
plt.legend()
plt.grid()
plt.show()

# gráfica conejos vs presas
plt.plot(xi,yi)

plt.title('Modelo presa-predador [xi,yi]')
plt.xlabel('x presa')
plt.ylabel('y predador')
plt.grid()
plt.show()