# -*- coding: utf-8 -*-
"""
Created on Mon Feb 6 2023

@author: Vale
"""

matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

matriz[0].append(sum(matriz[0][:3]))
matriz[1].append(sum(matriz[1][:3]))
matriz[2].append(sum(matriz[2][:3]))
matriz[3].append(sum(matriz[3][:3]))