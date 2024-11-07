def seleccionar_postulantes():
    genero = input("Introduce tu género (M/F): ").upper()
    edad = int(input("Introduce tu edad: "))
    altura = float(input("Introduce tu altura en metros: "))
    peso = float(input("Introduce tu peso en kg: "))
    puntaje = int(input("Introduce tu puntaje en la prueba: "))

    if genero == "F" and edad >= 18 and altura >= 1.6 and 55 <= peso <= 60 and puntaje > 65:
        print("Seleccionada para la Marina de Guerra del Perú.")
    elif genero == "M" and edad >= 18 and altura >= 1.65 and 55 <= peso <= 60 and puntaje > 65:
        print("Seleccionado para la Marina de Guerra del Perú.")
    else:
        print("No seleccionado.")