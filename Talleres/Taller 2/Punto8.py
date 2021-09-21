import numpy as np
import scipy.linalg as sp

def PivoteoParcial(A,B,k):
    
    mayor = 0
    mayorA = -1000
    indiceM = 0
    con = 0
    
    while(k != len(A)-1):  

        for i in range (len(A)-k): 
            mayor = abs(A[i+k][k])
              
            if mayorA < mayor:
                mayorA = mayor
                indiceM = i+k
        
        if(mayorA != A[k][k]):    
            temp = np.copy(A[k])
            A[k] = A[indiceM]
            A[indiceM] = temp  
            con+=1 
            tempa = np.copy(B[k])
            B[k] = B[indiceM]
            B[indiceM] = tempa              
        k+=1
                  
    return A,B

def Gauss(A,B):
    
    A = np.array(A,dtype=np.longdouble) 
    Acon  = np.concatenate((A,B),axis=1)
    tamano = np.shape(Acon)
    n = tamano[0]
    m = tamano[1]
    
    for i in range(0,n-1,1):
        p   = np.longdouble(Acon[i,i])
        adelante = i + 1
       
        for k in range(adelante,n,1):
            factor  = np.longdouble(Acon[k,i]/p)
            Acon[k,:] = np.longdouble(Acon[k,:] - Acon[i,:]*factor)
    
    ultfila = n-1
    ultcolumna = m-1
    X = np.zeros(n,dtype=np.longdouble)
    
    for i in range(ultfila,0-1,-1):
        suma = 0
        
        for j in range(i+1,ultcolumna,1):
            suma = np.longdouble(suma + Acon[i,j]*X[j])
            
        b = np.longdouble(Acon[i,ultcolumna])
        X[i] = np.longdouble((b-suma)/Acon[i,i])
    
    X = np.transpose([X])
    Y = Acon
  
    return X, Y

def Crammer(A,B):
 
    x = np.zeros(len(B))
    Da = np.linalg.det(A)
    
    #Igualar formato ingresado
    b = [0,0,0]

    for i in range(len(B)):
        b[i] = B[i][0]
        
    for i in range (len(b)):
        aux = A.copy()
        aux[:,i] = b
        auxB = np.linalg.det(aux)
        x[i]=auxB/Da
    
    R = [[0],[0],[0]]
    
    for i in range (len(R)): #Retornar en formato normal
        R[i][0] = x[i]
            
    return R

def FLU (A, B):
    
    A = A.tolist()
    for i in range(len(A)): #Convertir formato
        A[i].append(B[i][0])  
    A = np.array(A)   
       
    P, L, U = sp.lu(A)
    Acon = U
    
    tamano = np.shape(Acon)
    n = tamano[0]
    m = tamano[1]
    X = np.zeros(n,dtype=np.longdouble)
    
    ultfila = n-1
    ultcolumna = m-1
    
    for i in range(ultfila,0-1,-1):
        suma = 0
        
        for j in range(i+1,ultcolumna,1):
            suma = np.longdouble(suma + Acon[i,j]*X[j])
            
        b = np.longdouble(Acon[i,ultcolumna])
        X[i] = np.longdouble((b-suma)/Acon[i,i])
    
    X = np.transpose([X])
    return P,L,U,X

def errorAtras(A, B, X):
    
    AX = np.longdouble(np.dot(A,X))
    aux = [[0],[0],[0]]
    
    for i in range(len(a)):
        aux[i][0] = round((AX[i][0]),50)
        
    Resta = AX-B
    Error = sp.norm(Resta)
    Error = round((Error),100)
    print("\nError relativo hacia atras: " ,Error)
    
def errorAdelante(A, B, X):
    exacta = sp.solve(A,B)
    Error = sp.norm((exacta - X))
    print("\nError relativo hacia adelante es: " ,Error)

def numeroCondicion(A):
    
    Ainv = sp.inv(A)
    NuCond = (sp.norm(A))*(sp.norm(Ainv))
    print("\nNumero de condicion: ", NuCond)



# Gauss con pivoteo parcial

A1 = np.array([[1,-8,-2],[1,1,5],[3,-1,1]], float)
B1 = np.array([[1],[4],[-2]], float)

A1 = np.array([[1,4,0],[0,1,1],[2,0,3]], float)
B1 = np.array([[5],[2],[0]], float)

A1 = np.array([[1,3,-1],[4,-1,1],[1,1,7]])
B1 = np.array([[18],[27.34],[16.2]])

print("\n\n------- Metodo Gauss con pivoteo parcial ---------\n")
Acon = np.concatenate((A1,B1), axis=1)

print("Matriz inicial\n\n", Acon)

A,B = PivoteoParcial(A1,B1,0)
Acon = np.concatenate((A,B), axis=1)
print("\nMatriz con pivoteo parcial\n\n", Acon)

a,c = Gauss(A,B)

x = round((a[0][0]),100)
aux = [[0],[0],[0]]
for i in range(len(a)):
    aux[i][0] = round((a[i][0]),100)

print("\nResultados:\n\n", aux)

errorAtras(A1,B1,aux)
errorAdelante(A1, B1, aux)
numeroCondicion(A1)


# Gauss
A1 = np.array([[1,-8,-2],[1,1,5],[3,-1,1]], float)
B1 = np.array([[1],[4],[-2]], float)

A1 = np.array([[1,4,0],[0,1,1],[2,0,3]], float)
B1 = np.array([[5],[2],[0]], float)

A1 = np.array([[1,3,-1],[4,-1,1],[1,1,7]])
B1 = np.array([[18],[27.34],[16.2]])

print("\n\n------ Metodo Gauss  ---------\n")
Acon = np.concatenate((A1,B1), axis=1)
print("Matriz inicial\n\n", Acon)

a,c = Gauss(A1,B1)
print("\nGauss:\n\n", c)

x = round((a[0][0]),100)
aux = [[0],[0],[0]]
for i in range(len(a)):
    aux[i][0] = round((a[i][0]),100)

print("\nResultados:\n\n", aux)

errorAtras(A1,B1,aux)
errorAdelante(A1, B1, aux)
numeroCondicion(A1)


# Cramer

A1 = np.array([[1,-8,-2],[1,1,5],[3,-1,1]], float)
B1 = np.array([[1],[4],[-2]], float)

A1 = np.array([[1,4,0],[0,1,1],[2,0,3]], float)
B1 = np.array([[5],[2],[0]], float)

A1 = np.array([[1,3,-1],[4,-1,1],[1,1,7]])
B1 = np.array([[18],[27.34],[16.2]])

print("\n\n------ Metodo crammer ---------\n")
Acon = np.concatenate((A1,B1), axis=1)
print("Matriz inicial\n\n", Acon)

R = Crammer(A1,B1)
print("\nResultados\n\n", R)

errorAtras(A1,B1,R)
errorAdelante(A1, B1, R)
numeroCondicion(A1)


#   Factorización LU
A1 = np.array([[1,-8,-2],[1,1,5],[3,-1,1]], float)
B1 = np.array([[1],[4],[-2]], float)

A1 = np.array([[1,4,0],[0,1,1],[2,0,3]], float)
B1 = np.array([[5],[2],[0]], float)

A1 = np.array([[1,3,-1],[4,-1,1],[1,1,7]])
B1 = np.array([[18],[27.34],[16.2]])
print("\n\n------ Metodo Factorización LU ---------\n")
Acon = np.concatenate((A1,B1), axis=1)
print("Matriz inicial\n\n", Acon)

P,L,U,X = FLU(A1,B1)
print("\nMatriz L\n\n", L)
print("\nMatriz U\n\n", U)
print("\nMatriz LxU\n\n", L.dot(U))

x = round((a[0][0]),100)
aux = [[0],[0],[0]]
for i in range(len(X)):
    aux[i][0] = round((X[i][0]),100)

print("\nResultados\n\n", aux)

errorAtras(A1,B1,aux)
errorAdelante(A1, B1, aux)
numeroCondicion(A1)












