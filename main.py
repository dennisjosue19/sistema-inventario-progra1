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

    if opcion == 1:
        #CON ESTE CONDICIONAL VALIDAMOS QUE EL STOCK SE MANTENGA ABAJO DE 15 OBJETOS PARA PRACTICIDAD DEL EJERCICIO
        if len(inventario) > 2:
            print("Inventario lleno!!!")
        else:
            #En este bloque de codigo creamos un videojuego nuevo, asignando un codigo al azar si es que el juego no esta en stock
            #validando que los usuarios ingresen un nombre, plataforma, cantidad y precio validos al sistema
            codigo = generar_codigo(inventario)

            nombre = input("Ingresa el nombre del videojuego: ").strip().lower()
            while nombre == "":
                nombre = input("Nombre no valido, por favor ingresa el nombre del videojuego: ")

            plataforma = input("Ingresa la plataforma del videojuego: ").strip().lower()
            while plataforma == "":
                plataforma = input("Nombre no valido, por favor ingresa el nombre del videojuego: ")

            cantidad = int(input("Numero de unidades a ingresar: "))
            while cantidad <= 0:
                cantidad = int(input("Ingrese una cantidad valida: "))

            precio = float(input("Ingresa el precio del videojuego: "))
            while precio <= 0:
                precio = float(input("Ingrese un precio valido: "))

        #En las siguientes lineas validamos si un videojuego ya esta registrado en el inventario o no, si ya se encuentra dentro del inventario solo se suman
        # las cantidades que se van a ingresar y sino, el codigo crea el registro del nuevo videojuego asignando un codigo nuevo con la funcion generar_codigo
        encontrado = False
        for videojuego in inventario:
            if nombre == videojuego["nombre"] and plataforma == videojuego["plataforma"]:
                videojuego["cantidad"] = cantidad + videojuego["cantidad"]
                encontrado = True
                print("Videojuego existente. Cantidad actualizada con exito!")
                break

        if not encontrado:
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
        #EN ESTE BLOQUE DE CODIGO DECLARAMOS UNA BAJA DE INVENTARIO
        codigo_retirar = int(input("Ingresa el codigo del videojuego que quieres retirar del inventario: "))

        #CON ESTE CONDICIONAL VALIDAMOS QUE EL CODIGO SEA UN VALOR ENTERO VALIDO
        while codigo_retirar <= 0:
            try:
                codigo_retirar = int(input("Ingresa el codigo del videojuego a retirar"))
            except:
                print("Ingresa un codigo valido")

        cantidad_retirar = int(input("Numero de unidades a retirar: "))

        #AQUI VALIDAMOS SI EL CODIGO EXISTE, SINO IMPRIME UN MENSAJE EN PANTALLA QUE EL CODIGO NO EXISTE Y QUE EL USUARIO VALIDE SI ES CORRECTO
        if codigo_retirar != videojuego["codigo"]:
            print("El video juego no existe en el inventario, por favor verifique que el codigo sea correcto!")

        #AQUI VALIDAMOS SI EL STOCK QUE TENEMOS ES SUFICIENTE PARA SATISFACER LA DEMANDA, SI SE VALIDA SE DESCUENTA EL STOCK DEL INVENTARIO, SINO
        #IMPRIME UN MENSAJE EN PANTALLA QUE NO HAY UNIDADES SUFICIENTES
        if cantidad_retirar > videojuego["cantidad"]:
            print("No hay copias suficientes para satisfacer la demanda, intente mas tarde o espere que agreguen mas unidades al stock!!!")
        else:
            encontrado = False
            for videojuego in inventario:
                if codigo_retirar == videojuego["codigo"]:
                    videojuego["cantidad"] = videojuego["cantidad"] - cantidad_retirar
                    encontrado = True
                    print("Videojuego retirado de stock. Cantidad actualizada con exito!")
                    #ESTE CONDICIONAL VALIDA UNA REGLA DE NEGOCIO QUE AL HABER MENOS DE 5 UNIDADES EL SISTEMA IMPRIME UN MENSAJE EN PANTALLA
                    #AVISANDO QUE HAY UN STOCK BAJO
                    if videojuego["cantidad"] < 5:
                        print(f"Stock bajo en {videojuego["nombre"]}, con una cantidad de {videojuego['cantidad']}")
                    break
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
