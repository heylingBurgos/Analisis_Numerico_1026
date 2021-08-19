#import matplotlib.pyplot as plt
from sympy import *
from sympy.plotting import plot_parametric 
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) 


def Parametrica (): #Funcion utilizada para graficar funciones parametricas
    t = symbols('t')
    c=4     
    xa = 3*(sin(t))**3-1
    ya = 4*sin(t)*cos(t)  
    plot_parametric(xa, ya, (t, -c, c))
