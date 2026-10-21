print("Proyecto de programacion 1 - Sistema de inventario")

import random, json

print("=== Bienvenido a su sistema de inventario ===")
inventario = []
stock_minimo = 0
stock_maximo = 0

def generar_codigo(inventario):
    while True:
        codigo = random.randint(1000,9999)
        repetido = False
        for videojuego in inventario:
            if videojuego["codigo"] == codigo:
                repetido = True
                break
        if not repetido:
            return codigo

while True:
    print("==== MENU ====")
    print("1. Ingresar un videojuego: ")
    print("2. Sacar un videojuego: ")
    print("3. Buscar un videojuego: ")
    print("4. Mostrar inventario.")
    print("5. Obtener reporte de inventario.")
    print("6. Salir")

    try:
        opcion = int(input("Selecciona la accion a realizar: "))
    except ValueError:
        print("Ingresa una opcion valida")
        continue

    if opcion == 1:
        if stock_maximo > 2:
            print("Inventario lleno!!!")
            break
        else:
            codigo = generar_codigo(inventario)
            nombre = input("Ingresa el nombre del videojuego: ").strip().lower()
            plataforma = input("Ingresa la plataforma del videojuego: ").strip().lower()
            cantidad = int(input("Numero de unidades a ingresar: "))
            precio = float(input("Ingresa el precio del videojuego: "))

        encontrado = False
        for videojuego in inventario:
            if nombre == videojuego["nombre"] and plataforma == videojuego["plataforma"]:
                videojuego["cantidad"] = cantidad + videojuego["cantidad"]
                encontrado = True
                print("Videojuego existente. Cantidad actualizada con exito!")
                break

        if not encontrado:
            stock_maximo += 1
            nuevo_videojuego = {
                "codigo": codigo,
                "nombre": nombre,
                "plataforma": plataforma,
                "cantidad": cantidad,
                "precio": precio
            }
            inventario.append(nuevo_videojuego)
            print("Videojuego guardado con exito!")

    elif opcion == 2:
        print("¿Que videojuego desea sacar de inventario?")
        codigo_retirar = int(input("Ingresa el codigo del videojuego: "))
        encontrado = False
        for videojuego in inventario:
            if codigo_retirar == videojuego["codigo"]:
                videojuego["cantidad"] = cantidad + videojuego["cantidad"]
                encontrado = True
                print("Videojuego existente. Cantidad actualizada con exito!")
                break
    elif opcion == 3:
        print("Aun testing")
    elif opcion == 4:
        print("Mostrando inventario disponible...")
        if len(inventario) == 0:
            print("Inventario no existente")
        else:
            for videojuego in inventario:
                print("==========================================================")
                print("Codigo: ", videojuego["codigo"])
                print("Nombre: ", videojuego["nombre"])
                print("Plataforma: ", videojuego["plataforma"])
                print("Cantidad: ", videojuego["cantidad"])
                print("Precio: ", videojuego["precio"])
                print("==========================================================")
    elif opcion == 5:
        print("Generando reporte...")
    elif opcion == 6:
        print("Saliendo del inventario... Hasta pronto!!!!")
        break
    else:
        print("Opcion no valida, por favor ingrese una opcion valida")

