# Práctica 03: Python - Estructuras Condicionales

# Descripción
# En esta práctica se explorará la introducción a listas y estructuras condicionales en Python.

# Objetivos
# 1. Introducción al uso de listas.
# 2. Uso de estructuras condicionales: `if`, `elif`, `else`.

# Introducción a Listas
# Una lista en Python es una colección ordenada de valores. Los valores pueden ser de cualquier tipo.
# A continuación, veremos cómo crear y manipular listas.

# Crear una lista
mi_lista = [10, 20, 30, 40]
print("Lista original:", mi_lista)

# Acceder al primer elemento de la lista
print("Primer elemento:", mi_lista[0])

# Modificar un elemento en la lista
mi_lista[2] = 35
print("Lista modificada:", mi_lista)

# Adicionar elementos a una lista
mi_lista.append(50)
print("Lista después de adicionar un elemento:", mi_lista)

# Borrar un elemento de una lista
del mi_lista[1]
print("Lista después de eliminar el segundo elemento:", mi_lista)

# Ordenar una lista
mi_lista.sort()
print("Lista ordenada:", mi_lista)

# Longitud de una lista
print("Longitud de la lista:", len(mi_lista))

# Estructuras Condicionales

# Condición Simple (if)
numero = 5
if numero > 0:
    print("El número es positivo.")

# Condición if-else
numero = -3
if numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo o cero.")

# Condición Anidada (if-else)
numero = -5
if numero != 0:
    if numero > 0:
        print("El número es positivo.")
    else:
        print("El número es negativo.")
else:
    print("El número es cero.")

# Condición Encadenada (if-elif-else)
calificacion = 85
if calificacion >= 90:
    print("Calificación: A")
elif calificacion >= 80:
    print("Calificación: B")
elif calificacion >= 70:
    print("Calificación: C")
elif calificacion >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")
