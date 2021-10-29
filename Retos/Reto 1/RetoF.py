
import pandas as pd
import numpy as np
import math 
import matplotlib.pyplot as plt
import scipy.interpolate as spi
from scipy.spatial import distance as jc

def clasificarDatos(nombreArchivo, nombreHoja, col1, col2, col3):
    dF = pd.read_excel(nombreArchivo, sheet_name=nombreHoja, usecols=[col1, col2, col3])
    Rcol1 = dF.get(col1)
    Rcol2 = dF.get(col2)
    Rcol3 = dF.get(col3)
    Rcol1 = list(Rcol1)
    Rcol2 = list(Rcol2)
    Rcol3 = list(Rcol3)
    return Rcol1, Rcol2, Rcol3

def eliminarPorcentajeDatos(porcentaje, indices, columna1, columna2, columna3):
    datosEliminar = int(porcentaje*len(columna1))
    restantes = []
    
    for i in range(10, datosEliminar):
        A = np.random.randint(10, len(columna1)-10)
        restantes.append((columna1[i], columna2[i]))
        indices = np.delete(indices, A, 0)
        columna1 = np.delete(columna1, A, 0)
        columna2 = np.delete(columna2, A, 0)
        columna3 = np.delete(columna3, A, 0)
    return indices, columna1, columna2, columna3, restantes

def errorMed(original, interpolado):
    emc=0
    for i in range (len(original)):
        emc += pow(interpolado[i]-original[i],2)
    
    return math.sqrt(emc/2) 
 
def errorMinMax(original, interpolado):
    
    error=[]
    erroraux=[]
    contador=0
    for i in range(len(original)):
        resta = abs(interpolado[i]-original[i])
        if resta > 0:
            error.append(resta)
            erroraux.append(resta)
            
        contador+=1
        if contador == 100:
            print("error en el rango ",(i+1)-contador,"-",i+1, "maximo: ",round(max(erroraux),2),"y minimo: ",round(min(erroraux),2))
            contador=0
            erroraux.clear()
    print("Error maximo: {} y minimo: {} general".format(round(max(error),2),round(min(error),2) ))
    
    media=sum(error)/len(original)
    errorAbs=0
    for i in error:
        errorAbs+=abs(media-i)
    print("El error absouluto es: ",round(errorAbs/len(error),2))
    



#Extraer datos                                                            
DC1P, DC2P, DC3P = clasificarDatos("Datos.xls", "Itatira", "Dia Juliano", "Temp. Interna (ºC)", "Hora")

#Guardar datos originales
xP = np.arange(0, len(DC2P),1) #Indices
DatosOr1P = DC1P.copy()
DatosOr2P = DC2P.copy()
DatosOr3P = DC3P.copy()

#Eliminar porcentaje de datos
p = 0.3 #Porcentaje
indices, columna1AP, columna2AP, columna3AP, eliminadoP = eliminarPorcentajeDatos(p, xP, DC1P,  DC2P, DC3P)

#Interpolaciónes
#Interpolacion cubica
s_pen = spi.splrep(indices, columna2AP) 
xn_pen = xP
yn_pen = spi.splev(xn_pen, s_pen)
yn_pen=np.round(yn_pen,2)
#Interpolacion cuadratica
f = spi.interpolate.interp1d(indices, columna2AP, kind = 'quadratic')
xnew = xP
ynew = f(xnew)
ynew=np.round(ynew,2)


#Datos originales cuadratica y cubica
plt.figure(dpi = 1000)
plt.plot(xP, DatosOr2P, 'k-') #Datos originales
plt.plot(xn_pen, yn_pen, 'r-') #IC
plt.plot(xnew, ynew, 'c-')
plt.xlabel("Índice Calculado")
plt.ylabel("Temperatura Interna")
plt.title("Primer punto - Estacion Itatira")
plt.legend(['D Originales', 'I Cubica', 'I Cuadratica',])
plt.show()

#Datos originales cubico
plt.figure(dpi = 150)
plt.plot(xP, DatosOr2P, 'k-') #Datos originales
plt.plot(xn_pen, yn_pen, 'r-') #IC
plt.xlabel("Índice Calculado")
plt.ylabel("Temperatura Interna")
plt.title("Original vs Cubico - Estacion Itatira")
plt.legend(['D Originales', 'I Cubica'])
plt.show()

#Datos originales cuadratica
plt.figure(dpi = 150)
plt.plot(xP, DatosOr2P, 'k-') #Datos originales
plt.plot(xnew, ynew, 'c-')
plt.xlabel("Índice Calculado")
plt.ylabel("Temperatura Interna")
plt.title("Original vs cuadratica - Estacion Itatira")
plt.legend(['D Originales', 'I Cuadratica'])
plt.show()

#SEGUDO PUNTO
#Extraer datos    
DC1S, DC2S, DC3S = clasificarDatos("Datos.xls", "Quixadá", "Dia Juliano", "Temp. Interna (ºC)", "Hora")

#Guardar datos originales
xS = np.arange(0, len(DC2S),1) #Indices
DatosOr1S = DC1S.copy()
DatosOr2S = DC2S.copy()
DatosOr3S = DC3S.copy()

#Eliminar porcentaje de datos
p = 0.3 #Porcentaje
indicesS, columna1AS, columna2AS, columna3AS, eliminadoS= eliminarPorcentajeDatos(p, xS, DC1S, DC2S, DC3S)

#Ajuste de datos para el segundo punto
listaXP = xS
listaYP = DC2S


#ERRORES punto 1
print("Errores punto uno:")
print("----------------------------------------------------------------------------")
print("Indice de jaccard, datos originales - interpolacion cubica",jc.jaccard(DatosOr2P , yn_pen))
print("Indice de jaccard, datos originales - interpolacion cuadratica",jc.jaccard(DatosOr2P , ynew))
print("Indice de jaccard, interpolacion cubica - interpolacion cuadratica",jc.jaccard(yn_pen , ynew))
print("----------------------------------------------------------------------------")
print("Error medio cuadratico interpolacion cubica:",round(errorMed(DatosOr2P, yn_pen),2))
print("Error medio cuadratico interpolacion cuadratica:",round(errorMed(DatosOr2P, ynew),2))
print("Errores interpolacion cubica:")
errorMinMax(DatosOr2P, yn_pen)
print("..............................................")
print("Errores interpolacion cuadratica:")
errorMinMax(DatosOr2P, ynew)


'''for i in range(len(columna2AS)):
    for j in range(0, len(DatosOr1P)):
        if (columna1AS[i] == DatosOr1P[j]) and (columna3AS[i] == DatosOr3P[j]):
            listaXP.append(indices[i])
            listaYP.append(DatosOr2P[j])'''

#Interpolaciónes
#Interpolacion cubica
#fc = spi.interpolate.interp1d(indicesS, columna2AS, kind = 'cubic')
#xn_pen = xP
#yn_pen = fc(xn_pen)

s_pen = spi.splrep(xP, listaYP) 
xn_pen = listaXP
yn_pen = spi.splev(xn_pen, s_pen)
yn_pen=np.round(yn_pen,2)


#Interpolacion cuadratica
fs = spi.interpolate.interp1d(indicesS, columna2AS, kind = 'quadratic')
xnew = xP
ynew = fs(xnew)
ynew=np.round(ynew,2)

#Datos originales cuadratica y cubica
plt.figure(dpi = 1000)
plt.plot(xS, DatosOr2S, 'k-') #Datos originales
plt.plot(xn_pen, yn_pen, 'r-') #IC
plt.plot(xnew, ynew, 'c-')
plt.xlabel("Índice Calculado")
plt.ylabel("Temperatura Interna")
plt.title("Segundo punto - Estación Quixada")
plt.legend(['D Originales', 'I Cubica', 'I Cuadratica',])
plt.show()

#Datos originales cubico
#plt.figure(dpi = 1000)
plt.plot(xS, DatosOr2S, 'k-') #Datos originales
plt.plot(xn_pen, yn_pen, 'r-') #IC
plt.xlabel("Índice Calculado")
plt.ylabel("Temperatura Interna")
plt.title("Original vs Cubico - Estación Quixada")
plt.legend(['D Originales', 'I Cubica'])
plt.show()

#Datos originales cuadratica
#plt.figure(dpi = 1000)
plt.plot(xS, DatosOr2S, 'k-') #Datos originales
plt.plot(xnew, ynew, 'c-')
plt.xlabel("Índice Calculado")
plt.ylabel("Temperatura Interna")
plt.title("Original vs cuadratica - Estación Quixada")
plt.legend(['D Originales', 'I Cuadratica'])
plt.show()


#ERRORES punto 2
print("----------------------------------------------------------------------------")
print("Errores punto dos:")
print("----------------------------------------------------------------------------")
print("Indice de jaccard, datos originales - interpolacion cubica",jc.jaccard(DatosOr2S, yn_pen))
print("Indice de jaccard, datos originales - interpolacion cuadratica",jc.jaccard(DatosOr2S , ynew))
print("Indice de jaccard, interpolacion cubica - interpolacion cuadratica",jc.jaccard(yn_pen , ynew))
print("----------------------------------------------------------------------------")
print("Error medio cuadratico interpolacion cubica:",round(errorMed(DatosOr2S, yn_pen),2))
print("Error medio cuadratico interpolacion cuadratica:",round(errorMed(DatosOr2S, ynew),2))
print("Errores interpolacion cubica:")
errorMinMax(DatosOr2P, yn_pen)
print("..............................................")
print("Errores interpolacion cuadratica:")
errorMinMax(DatosOr2P, ynew)

'''
#otras metricas - Ajuste de curvas 
#Datos originales
#70% datos
z = np.polyfit(DC1P, DC2P,3) 
p = np.poly1d(z) 
yval = p(DC1P)  
z1 = np.polyfit(columna1AP, columna2AP,3) 
p1 = np.poly1d(z1) 
yval1 = p1(columna1AP)  
#Grafica de datos 
plt.figure(dpi=150) 
plt.plot(DC1P, DC2P, 'ko', ms = 2) 
plt.plot(DC1P, yval,'r-', label='Datos originales') 
plt.plot(columna1AP, yval1, 'b-', label = '70% Datos') 
plt.legend(loc=1) 
plt.title('Ajuste de curvas - Estación itatira') 
plt.show()
'''