
import numpy as np
import sympy as sp


def gaussseidel(A, b, tolerance=1e-16, max_iterations=1000000):

    x = np.zeros_like(b, dtype=np.double)

    #Iterate
    for k in range(max_iterations):

        x_old  = x.copy()

        #Loop over rows
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]

        #Stop condition 
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            break

    return x

def Cant_infectados(x):
    t = sp.symbols('t')
    f = x[0] * t+ x[1] * t **2 + x[2] * sp.exp(0.15 * t)
    rta = 0
    numero = 0
    dias=[]
    cantidad=[1500,1800,2000]
    
    while (rta < cantidad[0]):
        rta = f.evalf(subs={t:numero})
        numero = numero + 1
        
    dias.append(numero)
    rta = 0
    numero=0
    while (rta < cantidad[1]):
        rta = f.evalf(subs={t:numero})
        numero = numero + 1
        
    dias.append(numero)
    rta = 0
    numero=0
    while (rta < cantidad[2]):
        rta = f.evalf(subs={t:numero})
        numero = numero + 1
    dias.append(numero)
    
    for i in range (len(cantidad)):
        print ("\nEl día mas cercano donde la cantidad de persona supera los ",cantidad[i]," es el dia ", dias[i], "\n")


def infectados():
    A=np.array([[10,100,np.exp(1.5)],[15,225,np.exp(2.25)],[20,400,np.exp(3)]], float)
    b=[25,130,650]
    tol=10**-16
    x=gaussseidel(A, b, tol)
    Cant_infectados(x)




    

def main():
    print("solucion punto 3")
    infectados()
    
    

    
    
main()





