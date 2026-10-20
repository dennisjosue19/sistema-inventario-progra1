print("Proyecto de programacion 1 - Sistema de inventario")

import random, json

print("=== Bienvenido a su sistema de inventario ===")
inventario = []
stock_minimo = 5
stock_maximo = 15
archivo = "inventario.json"

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
        codigo = generar_codigo(inventario)
        nombre = input("Ingresa el nombre del videojuego: ").strip().lower()
        plataforma = input("Ingresa la plataforma del videojuego: ").strip().lower()
        cantidad = int(input("Numero de unidades a ingresar: "))
        precio = float(input("Ingresa el precio del videojuego: "))
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
        print("Aun testing")
    elif opcion == 3:
        print("Aun testing")
    elif opcion == 4:
        print("Mostrando inventario disponible...")
        print(inventario)
    elif opcion == 5:
        print("Generando reporte...")
    elif opcion == 6:
        print("Saliendo del inventario... Hasta pronto!!!!")
        break
    else:
        print("Opcion no valida, por favor ingrese una opcion valida")

