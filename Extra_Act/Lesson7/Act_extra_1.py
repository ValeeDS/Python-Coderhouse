# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 2023

@author: Vale
"""

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

#Borrar los elementos duplicados
lista_b = list(set(lista))

#Ordenar la lista de mayor a menor
lista_b.sort(reverse=True)

#Eliminar todos los números impares      
for i in range(len(lista_b) - 1, -1, -1):
    if lista_b[i] % 2 == 1:
        lista_b.pop(i)

#Realizar una suma de todos los números que quedan
suma = sum(lista_b)

#Añadir como primer elemento de la lista la suma realizada
lista_b.insert(0,suma)

#Devolver la lista modificada
print(lista_b)

#Finalmente, después de ejecutar la función, 
#comprueba que la suma de todos los números a partir del segundo, 
#concuerda con el primer número de la lista

print(lista_b[0] == sum(lista_b[1:5]))