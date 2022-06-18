
import random
"""Crear lista con 10 valores aleatorios"""

def insert10num(lista):
    for i in range(1, 11):
        lista.append(random.randint(1, 100))

def insert10numdif(diferente):
    for i in range(1, 11):
        diferente.append(random.randint(1, 100))


