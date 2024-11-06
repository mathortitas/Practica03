# Determinar si un número es positivo, negativo o cero
numero = int(input("Ingrese un número entero: "))
if numero > 0:
    resultado = "positivo"
elif numero < 0:
    resultado = "negativo"
else:
    resultado = "cero"
print(f"El número {numero} es {resultado}.")


# Entrada del usuario
radio = float(input("Ingrese el radio de un círculo: "))

# Menú de opciones
print("Seleccione una opción:")
print("a) Calcular el diámetro.")
print("b) Calcular el perímetro.")
print("c) Calcular el área.")
opcion = input("Ingrese su opción (a, b o c): ")

# Cálculo basado en la opción seleccionada
if opcion == "a":
    diametro = 2 * radio
    print(f"El diámetro del círculo es {diametro}.")
elif opcion == "b":
    perimetro = 2 * 3.14159 * radio
    print(f"El perímetro del círculo es {perimetro}.")
elif opcion == "c":
    area = 3.14159 * radio**2
    print(f"El área del círculo es {area}.")
else:
    print("Opción no válida. Elija entre 'a', 'b' o 'c'.")
