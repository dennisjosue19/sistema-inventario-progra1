print("Proyecto de programacion 1 - Sistema de inventario")

import random, json

print("=== Bienvenido a su sistema de inventario ===")

print("==== MENU ====")
print("1. Ingresar un videojuego: ")
print("2. Sacar un videojuego: ")
print("3. Buscar un videojuego: ")
print("4. Mostrar inventario.")
print("5. Obtener reporte de inventario.")
print("6. Salir")
opcion = int(input("Selecciona la accion a realizar: "))
inventario = []

while opcion !=6:
    if opcion == 1:
        codigo = random.randint(1000,9000)
        nombre = input("Ingresa el nombre del videojuego: ").lower()
        plataforma = input("Ingresa la plataforma del videojuego: ").lower()
        cantidad = int(input("Numero de unidades a ingresar: "))
        precio = float(input("Ingresa el precio del videojuego: "))
        print("Videojuego guardado con exito!")
        nuevo_videojuego = {
            "codigo": codigo,
            "nombre": nombre,
            "plataforma": plataforma,
            "cantidad": cantidad,
            "precio": precio
        }
        inventario.append(nuevo_videojuego)
        opcion = int(input("Selecciona la accion a realizar: "))

    elif opcion == 2:
        print("Aun testing")
        opcion = int(input("Selecciona la accion a realizar: "))
        pass
    elif opcion == 3:
        print("Aun testing")
        opcion = int(input("Selecciona la accion a realizar: "))
        pass
    elif opcion == 4:
        print("Mostrando inventario disponible...")
        print(inventario)
        print("Seleccione la accion a realizar:")
        opcion = int(input("Selecciona la accion a realizar: "))
    elif opcion == 5:
        print("Generando reporte...")
        opcion = int(input("Selecciona la accion a realizar: "))
        pass
    elif opcion == 6:
        print("Saliendo de inventario... Hasta pronto!!!")
    else:
        print("Opcion no valida, por favor ingrese una opcion valida")
        opcion = int(input("Selecciona la accion a realizar: "))

