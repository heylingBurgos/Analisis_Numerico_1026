import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def Secante (fx, t, a, b): #Recibe una funcion continua, tolerancia y un limite a y b
 
    i = 0 #Numero de iteraciones
    aux = 0
    puntos = []
 
    # Algoritmo 
    x0 = a #limite inferior
    x1 = b #limite superior
    x2 = np.clongdouble((x1) - ((fx(x1))*(x0-x1))/np.clongdouble(fx(x0) - fx(x1))) #Funcion evaluada en los limites actuales
    i += 1
    errorR = abs(np.clongdouble((x2-x1)/x2)) #Error
    
    while abs(np.clongdouble((x2-x1)/x2)) > t:  #Si el error es menor que la tolerancia se termina el ciclo y x2 toma el valor de la aproximación de la raiz.
        
        aux = errorR #Error anterior
        
        x0 = x1 #limite inferior
        x1 = x2 #limite superior
        x2 = np.clongdouble((x1) - ((fx(x1))*(x0-x1))/np.clongdouble(fx(x0) - fx(x1))) #Funcion evaluada en los limites actuales
        i += 1
        
        if i>2000000: #Si se llega al limite de iteraciones se rompe el ciclo y queda x2 actual como la raiz aproximada o un valor divergente
            aux = 1
            break
        
        errorR = abs(np.clongdouble((x2-x1)/x2)) #Error nuevo
        if i > 1:
            puntos.append((aux, errorR)) #Error relativo.
    
    print("\nMETODO SECANTE:\nLa raiz aproximada es: {} / Numero de iteraciones: {} / Tolerancia: {}".format(x1, i, t))
    if aux == 1:
        print("Diverge")
        
    # Grafico
    plt.xlabel("X")
    plt.ylabel("Y")
    x = np.arange(a, b, 0.1)
    plt.figure(0)
    plt.plot(x,fx(x))
    xs = np.linspace(a,b,100)
    horiz_line_data = np.array([0 for i in range(len(xs))])
    plt.plot(xs, horiz_line_data, 'r--') 
    plt.plot(x1, fx(x1), "ro")

    return puntos
        
