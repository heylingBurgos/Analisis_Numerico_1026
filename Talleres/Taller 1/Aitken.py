import numpy as np
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) 

def Aitken(fx, t, a, f): #Se recibe un funcion continua, tolerancia y un limite inicial. El valor f es un valor auxiliar para el funcionamiento el codigo
    
    i = 0
    aux = 0
    
    #Se halla el valor g(x) de cada una de las funciones.
    g1 = lambda x: (np.cos(x))
    g2 = lambda x: (np.exp(x))-1
    g3 = lambda x: (-3*x**3+6*x**2+(24/27))/4
    g4 = lambda x: (x**3-5)/2
    g5 = lambda x: (667.38*(1-np.exp(-0.146843*x))) / 40
    
    if f == 1:
        gx = g1
    elif f == 2:
        gx = g2   
    elif f == 3:
        gx = g3   
    elif f == 4:
        gx = g4
    elif f == 5:
        gx = g5
  
    # Algoritmo
    
    x0 = a
    x1 = np.clongdouble(gx(x0)) #Se evalua g(x) en el limite inicial
    x2 = np.clongdouble(gx(x1)) #El valor despues de evaluar g(x) en el limite inicial se vuelve a evaluar en el g(x)
    xn = np.clongdouble(x0 - (((x1-x0)**2)/((x2) -2*x1 + x0))) #Se usa la funcion de aitken con los valores hallados anteriormente.
    i += 1
    
    while abs(np.clongdouble((xn-x2)/xn)) > t: #Si el error es menor a la tolerancia se termina el ciclo y xn queda como el valor aproximado de la raiz.
        
        try:
        
            if i == 200000: #Si se llega al limite de iteraciones, xn toma el valor aproximado a la raiz o el valor divergente.
                xn = x0
                aux = 1
                break
            
            #Se hace lo mismo que en la primera iteracion, se evalua el g(x) con el limite actual, con el fin de hallar x0,x1 y x2 para poder hallar el xn.
            x0 = xn
            x1 = np.clongdouble(gx(x0))
            x2 = np.clongdouble(gx(x1))
            xn = np.clongdouble(x0 - (((x1-x0)**2)/((x2) -2*x1 + x0))) 
        
            if np.isinf(xn): #Si tiende a infinito se retorna xn que toma el valor aproximado a la raiz o el valor divergente.
                xn = x0
                aux = 2
                break
            
            if np.isnan(xn): #Si tiende a infinito se retorna xn que toma el valor aproximado a la raiz o el valor divergente.
                xn = x1
                aux = 2
                break
            
            if gx(xn) == 0: #Si el valor xn evaluado en g(x) es 0 se retorna el valor xn como la raiz.
                xn = x1
                break
        
            i += 1
         
        except ZeroDivisionError: #Si aparece una division en 0 se retorna el valor aproximado anterior de la raiz.
            xn = x0
            aux = 2
            break
            
            
    print("\nMETODO AIKTEN:\nLa raiz aproximada es: {} / Numero de iteraciones: {} / Toleracia: {}".format(xn, i, t))
    
    if aux == 2:
        print("Diverge por que tiende al infinito, ya que existe un division en 0")
    elif aux == 1:
        print("Diverge por que llego al limite de iteraciones")
    
    
