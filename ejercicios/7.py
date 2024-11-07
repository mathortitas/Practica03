def verificar_tuc():
    edad = int(input("Introduce tu edad: "))
    examen_medico = input("¿Aprobaste el examen médico? (S/N): ").upper() == "S"
    puntaje_conocimiento = int(input("Introduce tu puntaje en la prueba de conocimiento: "))
    puntaje_manejo = int(input("Introduce tu puntaje en la prueba de manejo: "))
    pago = int(input("Introduce el monto del pago (debe ser 10 soles): "))

    if edad >= 18 and examen_medico and puntaje_conocimiento > 80 and puntaje_manejo > 95 and pago == 10:
        print("APTO para obtener la Tarjeta Única de Circulación.")
    else:
        print("NO APTO para obtener la Tarjeta Única de Circulación.")