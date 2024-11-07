# Ejercicio 1: Verificar lista de compras de una juguería
def verificar_compras(jugueria, dia_actual):
    if dia_actual == "Lunes" and ("manzanas" in jugueria or "peras" in jugueria):
        print("Se puede desayunar jugo de manzanas o peras.")
    elif dia_actual == "Martes" and ("platano" in jugueria or "fresa" in jugueria) and "leche" in jugueria:
        print("Se puede desayunar jugo de leche con plátano o fresa.")
    elif dia_actual == "Miercoles" and "yogurt" in jugueria and "cereales" in jugueria:
        print("Se tomará yogurt con cereales.")
    elif dia_actual in ["Jueves", "Viernes", "Sábado", "Domingo"] and "papaya" in jugueria:
        print("Se puede desayunar jugo de papaya.")
    else:
        print("No se puede preparar desayuno con los ingredientes disponibles.")