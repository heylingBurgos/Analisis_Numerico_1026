import numpy as np

def steffensen(fx,t,a): #Se recibe una funcion continua, una tolerancia y un limite inicial.
    
    #x0 toma el valor de el limite inicial, y luego x0 se evalua en f(x) para hallar x1 y esos valores se usan en la funcion para hallar xn.
    x0= a
    x1= np.clongdouble(fx(x0))
    xt= np.clongdouble(x0-((x1**2)/(fx(x0+x1)-x1)))
    i=0
    aux = 0

    while(abs(x0-xt)>t): #Si el error es menor a la tolerancia se termina el ciclo y el valor de xt se retorna como el valor aproximado a la raiz.
        
        try:
            
            x1= np.clongdouble(xt) #Se evalua el valor aproximado de la raiz actual en f(x) para hallar x1.
            xt= np.clongdouble(x1-((fx(x1)**2)/(fx(x1+fx(x1))-fx(x1)))) #X1 se evalua en la funcion de steffensen para hallar el xn
            
            if i == 200000: #Si se llega al limite de iteraciones, xn toma el valor aproximado a la raiz o el valor divergente.
                xt = x1
                aux = 1
                break
            
            if np.isinf(xt): #Si tiende a infinito se retorna xn que toma el valor aproximado a la raiz o el valor divergente.
                xt = x1
                aux = 2
                break
            
            if np.isnan(xt): #Si tiende a infinito se retorna xn que toma el valor aproximado a la raiz o el valor divergente.
                xt = x1
                aux = 2
                break
            
            if fx(xt) == 0: #Si el valor xt evaluado en f(x) es 0 se retorna el valor xn como la raiz.
                break
  
            i+=1
                
        except ZeroDivisionError: #Si aparece una division en 0 se retorna el valor aproximado anterior de la raiz.
            xt=x1
            aux = 2
            break
        
        
    print("\nMETODO STEFFENSEN:\nLa raiz aproximada es: {} / Numero de iteraciones: {} / Toleracia: {}".format(xt, i, t))
    if aux == 2:
        print("Diverge por que tiende al infinito, ya que existe un division en 0")
    elif aux == 1:
        print("Diverge por que llego al limite de iteraciones")
