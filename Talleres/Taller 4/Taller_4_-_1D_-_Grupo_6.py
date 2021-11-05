from math import *
import numpy as np
import sympy as sp
import scipy.integrate as inte

#Definimos la funcion
#@ n: numero de x
#@ a y b los intervalos de la integral
#@ f: La funcion a integrar
def simpson13(n,a, b, f, ep):
    #calculamos h
    h = (b - a) / n
    #Inicializamos nuestra varible donde se almacenara las sumas
    suma = 0.0
    e=1
    i=0
    rest = 0
    inteo = inte.quad(f,a,b)
    while e>ep:
        #calculamos la x
        #x = a - h + (2 * h * i)
        x0 = a + i * h
        # si es par se multiplica por 4
        if(i % 2 == 0):
            suma = suma + 2 * fx(x0, f)
        #en caso contrario se multiplica por 2
        else:
            suma = suma + 4 * fx(x0, f)
        i+=1
        #sumamos los el primer elemento y el ultimo
        suma = suma + fx(a, f) + fx(b, f)
        #Multiplicamos por h/3
        rest = suma * (h / 3)
        e=inteo[0]-rest
    
    #Retornamos el resultado
    return (rest, i)

#Funcion que nos ayuda a evaluar las funciones
def fx(x, f):
    return f(x)
    
    

#valores de ejemplo para la funcion sin(x) con intervalos de
n=100000
a = 0.0
b = 2.0
f = lambda x: np.sqrt(1+np.cos(x)**2)
e=0.00001

resultado, i= simpson13(n, a, b, f, e)
print("El resultado de la integral es {} y se realizo en {} iteraciones".format(resultado,i))