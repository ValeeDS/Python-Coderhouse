# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 2023

@author: Vale
"""

cant = int(input("¿Cuántos números quiere introducir? "))
nums = []

for i in range(0,cant):
    nums.append(float(input("Ingrese el número ")))
    
media = sum(nums)/cant

print("La media aritmética es ", media)