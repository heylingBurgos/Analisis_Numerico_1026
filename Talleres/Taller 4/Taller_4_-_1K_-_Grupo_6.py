from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import scipy.integrate as inte


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
        e=abs(inteo[0])-rest
    
    #Retornamos el resultado
    return (rest, i)

#Funcion que nos ayuda a evaluar las funciones
def fx(x, f):
    return f(x)

def main():
    #definicion de puntos
    x1 = [0,4,8,16,20,24,28,32,36]
    y1 = [0,6,8,8.5,9,8,7,5,0]
    y2 = [0,-3,-2.5,-2.8,-3.4,-4.2,-4,-2.5,0]
    
    plt.plot(x1,y1)
    plt.plot(x1,y2)
    plt.tight_layout()
    plt.figure(dpi = 150)
    plt.show()
    
    #interpolacion lagrange para la obtencion del polinomio
    f1  = lagrange(x1, y1)
    f2 = lagrange (x1,y2)
    
    
    #Definicion de parametros para la funcion de simpson     
    n= 10000
    a = 0
    b = 36
    ep= 0.00000001
    valor1, i1 = simpson13(n, a, b, f1, ep)
    valor2, i2 = simpson13(n, a, b, f2, ep)
    total = abs(valor1)+abs(valor2)
    print("El area de aproximada afectada es de", total)

main()

        


