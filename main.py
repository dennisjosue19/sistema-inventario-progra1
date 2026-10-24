print("Proyecto de programacion 1 - Sistema de inventario")

#LIBRERIAS A UTILIZAR
import random, json

print("=== Bienvenido a su sistema de inventario ===")
inventario = []

#Funcion para generar un codigo al azar a nuevos videojuegos, el codigo recorre los videojuegos guardados en el la lista inventario, sino encuentra el videojuego
#la funcion genera un codigo nuevo pero si lo encuentra se salta la instruccion
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

#FUNCION QUE NOS AYUDA A VALIDAR NUMEROS ENTEROS EN LOS PROCESOS DE ALTAS, BAJAS, PEDIDO DE CODIGOS
def validar_entero(mensaje,minimo=1,maximo=100):
    while True:
        try:
            valor=int(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"El valor debe ser mayor o igual que {minimo}")
        except ValueError:
            print(f"Ingresa un numero valido!!")

def validad_precio(mensaje,minimo=1):
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"El valor debe ser mayor o igual que {minimo}")
        except ValueError:
            print(f"Ingresa un numero valido!!")

#ESTE BUCLE MUESTRA EL MENU EN PANTALLA E IMPRIME UN MENSAJE DE ERROR SI EL USUARIO INGRESA UNA OPCION QUE NO SEA VALIDA
while True:
    print("======== MENU =========")
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

    #BLOQUE DONDE DECLARAMOS UNA ALTA DE INVENTARIO
    if opcion == 1:
        nombre = input("Ingresa el nombre del videojuego: ").strip().lower()
        while nombre == "":
            nombre = input("Nombre no valido, por favor ingresa el nombre del videojuego: ").strip().lower()

        plataforma = input("Ingresa la plataforma del videojuego: ").strip().lower()
        while plataforma == "":
            plataforma = input("Nombre no valido, por favor ingresa el nombre del videojuego: ").strip().lower()

        cantidad = validar_entero("Ingresa el numero de unidades a ingresar al inventario: ")

        precio = validad_precio("Ingresa el precio del videojuego: ")

        encontrado = False
        for videojuego in inventario:
            if nombre == videojuego["nombre"] and plataforma == videojuego["plataforma"]:
                videojuego["cantidad"] = cantidad + videojuego["cantidad"]
                encontrado = True
                print("Videojuego existente. Cantidad actualizada con exito!")
                break
        if not encontrado:
            if len(inventario) > 2:
                print("Inventario lleno!!!")
            else:
                codigo = generar_codigo(inventario)
                #SE CREA EL REGISTRO DE UN JUEGO NUEVO Y LA VARIABLE STOCK MAXIMO AUMENTA EN UNO POR CADA JUEGO NUEVO
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
        codigo_retirar = validar_entero("Ingresa el codigo del videojuego a retirar del inventario: ")
        for videojuego in inventario:
            encontrado = False
            if codigo_retirar == videojuego["codigo"]:
                encontrado = True
                cantidad_retirar = validar_entero("Ingresa la cantidad de unidades a retirar del inventario: ")
                if cantidad_retirar > videojuego["cantidad"]:
                    print("De momento no hay unidades suficientes para completar el retiro, intentelo mas tarde.")
                else:
                    videojuego["cantidad"] = videojuego["cantidad"] - cantidad_retirar
                    print("Videojuego retirado de stock. Cantidad actualizada con exito!")
                    if videojuego["cantidad"] <= 5:
                        print(
                            f"Stock bajo en el videojuego: {videojuego['nombre']}, con una cantidad de {videojuego['cantidad']} unidad/es ")
                        break
            else:
                print("Videojuego no existe en el inventario, por favor revisar el codigo")
                codigo_retirar = validar_entero("Ingresa el codigo del videojuego a retirar del inventario: ")
            #ESTE CONDICIONAL VALIDA UNA REGLA DE NEGOCIO QUE AL HABER MENOS DE 5 UNIDADES EL SISTEMA IMPRIME UN MENSAJE EN PANTALLA
            #AVISANDO QUE HAY UN STOCK BAJO
    elif opcion == 3:
        print("Aun testing")
    elif opcion == 4:
        #ESTE BLOQUE MUESTRA EL INVENTARIO DISPONIBLE, SINO HAY NADA ALMACENADO IMPRIME UN MENSAJE EN PANTALLA QUE NO HAY NADA ALMACENADO
        print("Mostrando inventario disponible...")
        if len(inventario) == 0:
            print("Inventario no existente")
        else:
            #ESTE BLOQUE DE CODIGO MUESTRA LOS VIDEOJUEGOS ALMACENADOS Y AL FINAL LA CANTIDAD DE PRODUCTOS ALMACENADOS
            for videojuego in inventario:
                print("==========================================================")
                print("Codigo: ", videojuego["codigo"])
                print("Nombre: ", videojuego["nombre"])
                print("Plataforma: ", videojuego["plataforma"])
                print("Cantidad: ", videojuego["cantidad"])
                print("Precio: ", videojuego["precio"])
                print("==========================================================")
            print(f"Dentro de su inventario tiene {len(inventario)} juegos almacenados")
    elif opcion == 5:
        print("Generando reporte...")
    elif opcion == 6:
        print("Saliendo del inventario... Hasta pronto!!!!")
        break
