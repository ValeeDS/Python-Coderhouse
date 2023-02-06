# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 2023

@author: Vale
"""

usuario = {
    "nombre": input("Ingrese su nombre "),
    "edad": int(input("Ingrese su edad ")),
    "dirección": input("Ingrese su dirección ")
}

print(f"{usuario['nombre']} tiene {usuario['edad']}, y vive en {usuario['dirección']}")