import numpy as np

#Para evaluar biseccion los limites deben ser distintos, por ejemplo no puede ser [-1,1] o [-2,2], tiene que ser [-1,2] etc.

def Biseccion(fx, t, a, b): #Recibe una funcion continua, tolerancia y un limite a y b
 
    n = 0 #numero de repeticiones 
    aux = 0
    
    #Algoritmo
    
    x0 = a
    x2 = np.clongdouble((a+b)/2)
    y = 1
    n += 1
    
    while abs (np.clongdouble((b-a)/2)) > t : #Si el error es menor a la tolerancia se termina el ciclo y se retorna x2 como el valor aproximado de la raiz.
        
        auxx = np.clongdouble((b-a)/2) #error anterior.
        x2 = np.clongdouble((a+b)/2) #Se evalua x2 con los limites actuales.
        y = np.clongdouble(fx(x2)) #x2 se evalua en la funcion para saber su valor.
        
        if y == 0: #Si la funcion evaluada en x2 da 0 se retorna x2 como la raiz.
            break
        
        elif n == 2000000: #Si se llega a limite de iteraciones se retorna x2 como el valor aproximado de la raiz o el valor divergente
            aux = 1
            break
        
        else:
            #Se evaluan las funciones en el limite inferior y superior
            y1 = np.clongdouble(fx(x0))
            y2 = np.clongdouble(fx(x2))
            
            if np.clongdouble(y1*y2) < 0: #Se multiplican las funciones evaluadas anteriormente para determinar su determina signo. Si es negativo el rango superior pasa a ser x2 y si es positivo el rango inferior pasa a ser x2 
                b = x2  
              
            else: 
                a = x2
                
        xxxX = np.clongdouble((b-a)/2) #Error nuevo.
        
        if(auxx == xxxX): #si el error anterior es igual al error nuevo se termina el ciclo, todo esto ya que por la alta precision en algunos casos es imposible terminar el ciclo, ya que se queda en un valor mayor a la tolerancia y no disminuye, lo cual genera un bucle infinito.
            break
               
            #print("intervalo: [{}, {}]".format(x0, x1)) #Imprimir itervalo.
        n+=1
           
    print("\nMETODO BISECCIÒN:\nla raiz aproximada es: {} / Numero de iteraciones: {} / Tolerancia: {}".format(x2,n,t))
    
    if aux == 1:
        print("Diverge")






