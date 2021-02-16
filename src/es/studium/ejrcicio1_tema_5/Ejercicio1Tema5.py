#!/usr/bin/env python
# -- coding: utf-8 --
# 
#  format.py
#
'''
Created on 16 feb. 2021

@author: clja1
'''
'''Definir una funci�n max() que tome como argumento dos n�meros y
devuelva el mayor de ellos. (Es cierto que Python tiene una funci�n max()
incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.'''
print ("El número mayor")
x=int(input ("introduce un número entero: "))
y=int(input ("introduce otro número entero: "))
def fun (x,y):
    if x>y:
        return (x)
    elif y>x:
        return (y)
        
numeros=fun(x,y)
print ("El número mayor es: "+ str(numeros))
   
    
    
