# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:36:37 2021

@author: oscar
"""

# Integración por Método de Simpson 1/3 Compuesto

'''
Primeramente se definen los límites de integración con los cuales se quiere
trabajar.
'''
a=0.0     #Límite inferior
b=100.0   #Límite superior

'''
Se definen el número de subintervalos para el método numérico.
Cabe recalcar que este n debe ser par para el Método de Simpson.
'''
n=4

# Se determina el ancho para cada subintervalo

h=(b-a)/n

'''
Se define la función a integrar. En este caso se está tratando con un 
movimiento uniformemente aceelerado
'''
def f(t):
    return 0.005*t+0.5
'''
Se inicializa el valor para la sumatoria, en este caso ya se conocen los
pesos para la función evaluada en los extermos del intervalo
'''

sumatoria= (h/3)*(f(a)+f(b))

'''
Se realiza la sumatoria correspondiente al método de integración numérica,
estableciendo los pesos para cada iteración, dependiendo de si esta es par o
impar.
'''
for i in range(1,n):
    t_i=a+i*h # Se calcula el valor de t para cada iteración
    if (i % 2 == 0):
        sumatoria=sumatoria+(2/3)*h*f(t_i) #Si es par se multplica por 2/3
    else:
        sumatoria=sumatoria+(4/3)*h*f(t_i) ##Si es impar se multplica por 4/3
valorReal=75.0

print("El desplazamiento es  ",sumatoria)
print("Se tiene un error de ",abs(100*(valorReal-sumatoria)/valorReal))


        
