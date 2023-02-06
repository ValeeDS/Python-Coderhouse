# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 2023

@author: Vale
"""

num = int(input("Ingrese un número "))

while (num % 2 == 0):
    print("Número ingresado incorrecto. Intente nuevamente")
    num = int(input("Ingrese un número"))
    
print("Número ingresado correctamente")