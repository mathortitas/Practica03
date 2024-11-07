def verificar_acceso():
    nombres = ["Alice", "Bob", "Carlos"]
    contraseñas = ["1234", "abcd", "pass"]

    nombre = input("Introduce tu nombre: ")
    contraseña = input("Introduce tu contraseña: ")

    if nombre in nombres and contraseña in contraseñas:
        print("Bienvenido al sistema, trabajador de MicroSecret.")
    else:
        print("Acceso denegado.")
