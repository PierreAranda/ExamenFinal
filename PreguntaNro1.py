
import random
"""Crear lista con 10 valores aleatorios"""

def insert10num(lista):
    for i in range(1, 11):
        lista.append(random.randint(1, 100))

def insert10numdif(diferente):
    for i in range(1, 11):
        diferente.append(random.randint(1, 100))

milista2=[]
item2=insert10numdif(milista2)
milista2.sort()
milista2.reverse()

milista1=[]
item1=insert10numdif(milista1)
milista1.sort()

print("Mi lista de la funcion 2 es: ", milista2)
print("Mi lista del funcion 1 es: ", milista1)

def numeroMayor(listanummax):
    i = max(listanummax)
    return i

numeromaximo=numeroMayor(milista2)
print("El numero mayor de mi lista con la función 1 es: ", numeromaximo)



