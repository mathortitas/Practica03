# Ejemplos de Operaciones con Listas

# Concatenación de listas
lista1 = [10, 20, 30]
lista2 = [40, 50, 60]
print("Concatenación de listas:", lista1 + lista2)

# Mejorando la impresión de varias listas
listaA = ['audi', 'toyota', 'mazda']
puerta = [2, 4]
print("Mi auto es:", listaA[-1].title())
print(f"Mi auto {listaA[-2].title()} tiene {puerta[-2]} puertas")

# Operadores matemáticos en una lista
lista3 = [100, 500, 200, 7000, -200]
print("Suma de elementos:", sum(lista3))
print("Máximo de la lista:", max(lista3))
print("Mínimo de la lista:", min(lista3))

# Creación de listas con rangos
lista1 = list(range(7))           # lista de 0 a 6
lista2 = list(range(1, 10))       # lista de 1 a 9
lista3 = list(range(-10, 2))      # lista de -10 a 1
lista4 = list(range(200, 100, -20)) # lista de 200 a 100 restando 20
lista5 = list(range(200, 100, 20))  # lista vacía, rango no avanza

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)
print("Lista 4:", lista4)
print("Lista 5:", lista5)

# Ejemplo de error común en listas
autos = ['mazda', 'audi', 'toyota', 'subaru', 'bmw', 'lamborghini']
try:
    print(autos[6].upper())
except IndexError:
    print("Error: El índice está fuera del rango. Las listas en programación suelen empezar en 0")

# Solución al problema del índice
print(autos[4].upper())  # Acceso correcto dentro del rango

# Ejercicio: Determinar si un número es positivo, negativo o cero
x = int(input("Ingrese un número entero, positivo o negativo: "))
if x > 0:
    y = "positivo"
elif x < 0:
    y = "negativo"
else:
    y = "cero"
print(f"El número {x} es {y}")

# Ejemplo 2: Otra forma de detectar positivos, negativos o cero con una función simple
def detectar_numero(x):
    if x < 0:
        return 'negativo'
    elif x > 0:
        return 'positivo'
    else:
        return 'cero'

num = int(input("Ingrese un número entero, positivo o negativo: "))
print(f"El número {num} es {detectar_numero(num)}")

# Cálculo del perímetro, área y diámetro de un círculo

radio = float(input("Ingrese el radio de un círculo: "))

print("Seleccione una opción:")
print("a) Calcular el diámetro.")
print("b) Calcular el perímetro.")
print("c) Calcular el área.")
opcion = input("Elige a, b o c y presiona enter: ")

if opcion == "a":
    diametro = 2 * radio
    print(f"El diámetro del círculo es {diametro}.")
elif opcion == "b":
    perimetro = 2 * 3,1416 * radio
    print(f"El perímetro del círculo es {perimetro}.")
elif opcion == "c":
    area = 3,1416 * radio ** 2
    print(f"El área del círculo es {area}.")
else:
    print("Opción no válida. Solo hay tres opciones: a, b o c.")

# Verificación de lista de alimentos para parrillada
alimentos = ['arroz', 'papas', 'camotes', 'leche', 'carne', 'cebolla', 'tomate', 'lechuga']
if 'carne' in alimentos:
    print("Hoy comemos parrilla!")
else:
    print("Hoy comemos verduras")

# Verificación de disponibilidad de frutas en una juguería
frutas = ['platano', 'manzana', 'pera', 'naranja', 'mandarina', 'uva']
antojo = input("Ingrese la fruta que desea para su jugo: ").lower()
if antojo in frutas:
    print(f"Si tenemos {antojo.upper()}! Te prepararemos un jugo.")
else:
    print(f"No tenemos {antojo.upper()} hoy, vuelve mañana.")
print("Gracias por su preferencia!")

# Verificación de mayoría de edad
nombre = input("Ingresa tu nombre: ").capitalize()
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print(f"{nombre} es mayor de edad con {edad} años.")
else:
    print(f"{nombre} es menor de edad con {edad} años.")
