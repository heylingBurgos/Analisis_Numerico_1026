import Biseccion as B
import Secante as S
import Aitken as A
import Grafica_Parametrica as L
import numpy as np
import Steffensen as St
import matplotlib.pyplot as plt


def errorR(lista):
        xi, yi = zip(*lista)
        plt.figure(1)
        plt.title("Relacion entre errores relativos")
        plt.xlabel("ei")
        plt.ylabel("ei+1")
        plt.plot(xi, yi)

print("Selecciona la formula que deseas evaluar:")
print("\n1) cos(x)^2 - x^2 \n2) e^x-x-1 \n3) x^3-2x^2+4/3x-8/27 \n4) x^3-2x-5 \n5) (667.38)/x)(1-e^(-0.146843x))-40 \n6) f(x)= 3sin(t)^3 -1 | g(x)= 4sint(t)cos(t) - (Funciones parametricas)")
entrada = int(input("Ingrese el numero: "))

f1 = lambda x: (np.cos(x))**2-x**2
f2 = lambda x: np.exp(x)-x-1
f3 = lambda x: (x**3) -(2*x**2) + (4/3)*x - (8/27)
f4 = lambda x: ((x**3)-2*x-5)
f5 = lambda x: ((667.38)/x)*(1-np.exp(-0.146843*x))-40 
f6 = lambda x: 3*(np.sin(x)**3) - 1 - 4*np.sin(x)*np.cos(x) #Documento adjunto se explica como se realizo el procedimiento.

funciones = {1: f1, 2:f2,3:f3,4:f4,5:f5, 6:f6}

if entrada == 1:
    print("\nFuncion seleccionada: cos(x)^2 - x^2")
    t = input("Ingrese la toleracia deseada ej(10**-8): ")
    a = float(input("Ingrese el limite inferior: "))
    b = float(input("Ingrese el limite superior: "))
    lista = S.Secante(funciones[1], eval(t), a, b)
    B.Biseccion(funciones[1], eval(t), a, b)
    A.Aitken(funciones[1], eval(t), a, 1)
    St.steffensen(funciones[1],eval(t), a)
    errorR(lista)
    
elif entrada == 2:
    print("\nFuncion seleccionada: e^x-x-1")
    t = input("Ingrese la toleracia deseada ej(10**-8): ")
    a = float(input("Ingrese el limite inferior: "))
    b = float(input("Ingrese el limite superior: "))
    lista = S.Secante(funciones[2], eval(t), a, b)
    B.Biseccion(funciones[2], eval(t), a, b)
    A.Aitken(funciones[2], eval(t), a, 2)
    St.steffensen(funciones[2],eval(t), a)
    errorR(lista)

elif entrada == 3:
    print("\nFuncion seleccionada: x^3-2x^2+4/3x-8/27")
    t = input("Ingrese la toleracia deseada ej(10**-8): ")
    a = float(input("Ingrese el limite inferior: "))
    b = float(input("Ingrese el limite superior: "))
    lista = S.Secante(funciones[3], eval(t), a, b)
    B.Biseccion(funciones[3], eval(t), a, b)
    A.Aitken(funciones[3], eval(t), a, 3)
    St.steffensen(funciones[3],eval(t), a)
    errorR(lista)

elif entrada == 4:
    print("\nFuncion seleccionada: x^3-2x-5")
    t = input("Ingrese la toleracia deseada ej(10**-8): ")
    a = float(input("Ingrese el limite inferior: "))
    b = float(input("Ingrese el limite superior: "))
    lista = S.Secante(funciones[4], eval(t), a, b)
    B.Biseccion(funciones[4], eval(t), a, b)
    A.Aitken(funciones[4], eval(t), a, 4)
    St.steffensen(funciones[4],eval(t), a)
    errorR(lista)
    
elif entrada == 5:
    print("\nFuncion seleccionada: (667.38)/x)(1-e^(-0.146843x))-40")
    t = input("Ingrese la toleracia deseada ej(10**-8): ")
    a = float(input("Ingrese el limite inferior: "))
    b = float(input("Ingrese el limite superior: "))
    lista = S.Secante(funciones[5], eval(t), a, b)
    B.Biseccion(funciones[5], eval(t), a, b)
    A.Aitken(funciones[5], eval(t), a, 5)
    St.steffensen(funciones[5],eval(t), a)
    errorR(lista)
    
elif entrada == 6:
    print("\nFuncion seleccionada: f(x)= 3sin(t)^3 -1 | g(x)= 4sint(t)cos(t) - (Funciones parametricas)")
    t = input("Ingrese la toleracia deseada ej(10**-8): ")
    a = float(input("Ingrese el limite inferior: "))
    b = float(input("Ingrese el limite superior: "))
    L.Parametrica()
    lista = S.Secante(funciones[6], eval(t), a, b)
    B.Biseccion(funciones[6], eval(t), a, b)
    errorR(lista)
    
    
    

    

