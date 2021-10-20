# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:35:32 2021

@author: andre
"""

import numpy as np
import sympy as sp
import math
            

a = np.array([0, 0, 1, 2], float)
b = np.array([10, 10, 15, 5], float)
tan = 1
k = len(b)
res = np.zeros([k, k])
res[:,0] = b
for j in range(1, k):
    for i in range(k - j):
        if a[i+j] == a[i]:
            res[i][j] = tan / math.factorial(i)
        else:
            res[i][j] = (res[i+1][j-1] - res[i][j-1]) / (a[i+j]-a[i])

pol = 0
x = sp.Symbol('x')
for i in range(k):
    pol += res[0][i]*x**i
print("El polinomio de grado 3 que pasa por los puntos (0,3),(1,15) y (2,5) es:")
print()
print(pol)