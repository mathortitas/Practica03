def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    medio = len(numeros_ordenados) // 2
    if len(numeros_ordenados) % 2 == 0:
        return (numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2
    else:
        return numeros_ordenados[medio]

def calcular_frecuencia(numeros):
    frecuencia = {}
    for numero in numeros:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    return frecuencia

def estadisticas_numeros():
    numeros = [int(input("Introduce un número: ")) for i in range(20)]
    print("Seleccione una opción:\n1) Media\n2) Mediana\n3) Frecuencia")
    opcion = input("Opción: ")
    if opcion == "1":
        print("Media:", calcular_media(numeros))
    elif opcion == "2":
        print("Mediana:", calcular_mediana(numeros))
    elif opcion == "3":
        print("Frecuencia:", calcular_frecuencia(numeros))
    else:
        print("Opción no válida.")
