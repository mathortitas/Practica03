def verificar_materiales():
    almacen = ["clavos", "madera", "plancha metal", "soldadura"]

    if "clavos" in almacen and "madera" in almacen:
        print("Se puede construir una ventana.")
    elif "plancha metal" in almacen and "soldadura" in almacen:
        print("Se puede construir una puerta metálica.")
    elif "plancha de madera" in almacen and "madera" in almacen:
        print("Se puede construir una puerta.")
    else:
        print("Materiales insuficientes. Solicitar compra de materiales.")
