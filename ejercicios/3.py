def ordenar_objetos():
    objetos = [input("Introduce un objeto de casa: ") for _ in range(10)]
    print("Seleccione una opción:\n1) Orden ascendente\n2) Orden descendente")
    opcion = input("Opción: ")
    if opcion == "1":
        print("Objetos ordenados ascendentemente:", sorted(objetos))
    elif opcion == "2":
        print("Objetos ordenados descendentemente:", sorted(objetos, reverse=True))
    else:
        print("Opción no válida.")