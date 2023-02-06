# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:28:29 2023

@author: Vale
"""

num_1 = int(input("Ingrese un número: "))
num_2 = int(input("Ingrese otro número: "))

print("\nMENU\n\
\n\
1) Mostrar una suma de los dos números\n\
2) Mostrar una resta de los dos números (el primero menos el segundo)\n\
3) Mostrar una multiplicación de los dos números\n\
4) Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará\n")

option = int(input("Elija una opción del menú"))

while (option < 1 or option > 4):
    print("Opción no válida, ingrese nuevamente")
    option = int(input("Elija una opción del menú"))

while (option != 4):
    if option == 1:
        print("La suma de los dos números es", num_1 + num_2)
    elif option == 2:
        print("La resta de los dos números es", num_1 - num_2)#
    elif option == 3:
        print("La multiplicación de los dos números es", num_1 * num_2)
    option = int(input("Elija una opción del menú"))
    continue

print("Finalizó el programa")