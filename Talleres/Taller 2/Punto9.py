
import numpy as np
from scipy.sparse import csr_matrix
import random 
from numpy.linalg import norm
from scipy.sparse.linalg import cgs
from scipy.sparse.linalg import cg


def gradiente(A,b,x0,tol,n):
    d0 = b - np.dot(A,x0)
    r0 = d0
    x1 = x0
    k=1
    while(k<n):
        a0 = np.dot(r0,r0) / np.dot(np.dot(d0,A),d0)
        x1 = x0 + np.dot(a0,d0)
        r1 = r0 - np.dot(np.dot(a0,A),d0)
        if(norm(r1) <= tol):
            break
        b0 = np.dot(r1,r1) / np.dot(r0,r0)
        d1 = r1 + np.dot(b0,d0)
        x0, d0, r0 = x1, d1, r1
        k+=1
    return x1,k


#funcion para la creacion de una matriz disperza de nxn
def matriz_dipersa(n):
    '''A = np.identity(6)
    print(A)'''
    #a = np.diag(np.arange(1,1000,2))
    #print(a)
    
    a=[]
    b=[]
    c=[]
    d=[]
    guess = np.zeros(n, float)
    
    for i in range(0,n):
        a.append(random.randint(1, n-1))
        b.append(random.randint(1, n-1))
        c.append(random.randint(1, 100))
        d.append([random.randint(1, 100)])
        
    
    row = np.array(a)
    col = np.array(b)
    data = np.array(c)
    B = np.array(d)
    
    A=csr_matrix((data, (row, col)), shape=(n,n))
    D = A.todense()
   
    tol=10**-16    
    grad1,it1=gradiente(D,B,guess,tol,n)
    for i in range(len(grad1)):
        print("Solucion:",i+1,":", grad1[i,0],"\n")
    
def main():
    #n=int(input("Escriba el numero del tamaño de la matriz: \t"))
    n=100
    print("solucion punto 9 \n")
    matriz_dipersa(n)

main()