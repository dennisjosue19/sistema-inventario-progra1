print("Proyecto de programacion 1 - Sistema de inventario")

# LIBRERIAS A UTILIZAR
import random, json

print("=== Bienvenido a su sistema de inventario ===")
# PARA LA PERSISTENCIA CARGAMOS EL JSON AL PRINCIPIO DEL PROGRAMA
try:
    with open("inventario.json", "r") as archivo:
        inventario = json.load(archivo)
except FileNotFoundError:
    inventario = []

# Funcion para generar un codigo al azar a nuevos videojuegos, el codigo recorre los videojuegos guardados en el la lista inventario, sino encuentra el videojuego
# la funcion genera un codigo nuevo pero si lo encuentra se salta la instruccion
def generar_codigo(inventario):
    while True:
        codigo = random.randint(1000,9999)
        repetido = False
        for videojuego in inventario:
            if videojuego['codigo'] == codigo:
                repetido = True
                break
        if not repetido:
            return codigo

# FUNCION QUE NOS AYUDA A VALIDAR NUMEROS ENTEROS EN LOS PROCESOS DE ALTAS, BAJAS, PEDIDO DE CODIGOS
def validar_entero(mensaje,minimo=1):
    while True:
        try:
            valor=int(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"El valor debe ser mayor o igual que {minimo}")
        except ValueError:
            print(f"Ingresa un numero valido!!")

# FUNCION QUE AL IGUAL QUE LA ANTERIOR, NOS AYUDA CON LA VALIDACION DEL PRECIO DEL VIDEOJUEGO
def validar_precio(mensaje,minimo=1):
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"El valor debe ser mayor o igual que {minimo}")
        except ValueError:
            print(f"Ingresa un numero valido!!")

# FUNCION BUSQUEDA BINARIA
def busqueda_binaria(inventario, codigo):
    inicio = 0
    final = len(inventario) - 1
    while inicio <= final:
        centro = (inicio + final) // 2
        if codigo == inventario[centro]['codigo']:
            return inventario[centro]
        elif codigo > inventario[centro]['codigo']:
            inicio = centro + 1
        else:
            final = centro - 1
    return None

# ESTE BUCLE MUESTRA EL MENU EN PANTALLA E IMPRIME UN MENSAJE DE ERROR SI EL USUARIO INGRESA UNA OPCION QUE NO SEA VALIDA
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

    # BLOQUE DONDE DECLARAMOS UNA ALTA DE INVENTARIO
    if opcion == 1:
        # SE PIDEN LOS DATOS DEL VIDEOJUEGO NOMBRE, PLATAFORMA, CANTIDAD DE UNIDADES A INGRESAR, PRECIO
        nombre = input("Ingresa el nombre del videojuego: ").strip().lower()
        while nombre == "":
            nombre = input("Nombre no valido, por favor ingresa el nombre del videojuego: ").strip().lower()

        plataforma = input("Ingresa la plataforma del videojuego: ").strip().lower()
        while plataforma == "":
            plataforma = input("Nombre no valido, por favor ingresa el nombre de la plataforma: ").strip().lower()

        cantidad = validar_entero("Ingresa el numero de unidades a ingresar al inventario: ")

        precio = validar_precio("Ingresa el precio del videojuego: ")

        # EN ESTE BLOQUE VALIDAMOS SI EL PRODUCTO YA EXISTE SOLAMENTE SE AGREGA LA CANTIDAD DE UNIDADES A INGRESAR
        # SIN TENER QUE CREAR UN CODIGO
        encontrado = False
        for videojuego in inventario:
            if nombre == videojuego["nombre"] and plataforma == videojuego["plataforma"]:
                videojuego["cantidad"] = cantidad + videojuego["cantidad"]
                encontrado = True
                print("Videojuego existente. Cantidad actualizada con exito!")
                break
        # EN CASO EL PRODUCTO NO SE ENCUENTRE EN EL INVENTARIO, SE PROCEDE A CREAR EL REGISTRO DEL VIDEOJUEGO PERO ANTES VALIDAMOS
        # SI TENEMOS ESPACIO EN EL INVENTARIO PARA SEGUIR AGREGANDO PRODUCTOS CON UN LEN(INVENTARIO)
        if not encontrado:
            if len(inventario) > 14:
                print("Inventario lleno!!!")
            else:
                # AQUI SE CREA EL REGISTRO DEL VIDEOJUEGO
                codigo = generar_codigo(inventario)
                nuevo_videojuego = {
                    "codigo": codigo,
                    "nombre": nombre,
                    "plataforma": plataforma,
                    "cantidad": cantidad,
                    "precio": precio
                }
                inventario.append(nuevo_videojuego)
                print("Videojuego guardado con exito!")

    # EN ESTE BLOQUE SE REALIZAN LAS BAJAS DE INVENTARIO
    elif opcion == 2:
        # PREGUNTAMOS AL USUARIO EL CODIGO DEL VIDEOJUEGO QUE SE PUEDE ENCONTRAR USANDO LA OPCION 4 EN EL MENU PRINCIPAL
        codigo_retirar = validar_entero("Ingresa el codigo del videojuego a retirar del inventario: ")
        encontrado = False
        for videojuego in inventario:
            # SI EL CODIGO EXISTE DENTRO DEL INVENTARIO VALIDAMOS 3 POSIBILIDADES:
            if codigo_retirar == videojuego["codigo"]:
                encontrado = True
                # PRIMERA POSIBILIDAD: SI LA CANTIDAD SOLICITADA ES MAYOR QUE LA QUE HAY EN STOCK, EL PROGRAMA DA UN MENSAJE QUE
                # NO HAY STOCK SUFICIENTE PARA SUPLIR LA DEMANDA.
                cantidad_retirar = validar_entero("Ingresa la cantidad de unidades a retirar del inventario: ")
                if cantidad_retirar > videojuego["cantidad"]:
                    print("De momento no hay unidades suficientes para completar el retiro, intentelo mas tarde.")
                # LA SEGUNDA POSIBILIDAD ES PROCEDER A LA BAJA DE PRODUCTO DEL INVENTARIO DE MANERA EXITOSA, Y SI CUMPLE LA
                # REGLA DE NEGOCIO: AVISAR QUE HAY 5 O MENOS UNIDADES EN STOCK, IMPRIME UN MENSAJE QUE HAY STOCK BAJO.
                else:
                    videojuego["cantidad"] = videojuego["cantidad"] - cantidad_retirar
                    print("Videojuego retirado de stock. Cantidad actualizada con exito!")
                    if videojuego["cantidad"] <= 5:
                        print(f"Stock bajo en el videojuego: {videojuego['nombre']}, en la plataforma: {videojuego['plataforma']} con una cantidad de {videojuego['cantidad']} unidad/es ")
                break

        # TERCERA POSIBILIDAD, SI EL CODIGO NO EXISTE EL PROGRAMA DA UN MENSAJE DE ERROR.
        if not encontrado:
            print("Videojuego no existe en el inventario, por favor revisar el codigo")

    # AQUI UTILIZAMOS LA BUSQUEDA BINARIA PARA LA BUSQUEDA DE LOS VIDEOJUEGOS MEDIANTE UN CODIGO UNICO
    elif opcion == 3:
        # VALIDAMOS PRIMERO QUE HAYAN OBJETOS GUARDADOS SINO HAY IMPRIMIR UN MENSAJE
        if len(inventario) == 0:
            print("No hay videojuegos registrados")

        # EN ESTE BLOQUE PRIMERO ORDENAMOS LA LISTA POR CODIGO YA QUE ES REQUISITO QUE ESTE ORDENADA PARA USAR
        # LA BUSQUEDA BINARIA
        else:
            inventario.sort(key=lambda videojuego: videojuego["codigo"])
            codigo = validar_entero("Ingrese el codigo del videojuego: ")
            resultado = busqueda_binaria(inventario, codigo)

            # SI EL PROGRAMA ENCUENTRA EL CODIGO IMPRIME LOS DATOS DEL VIDEOJUEGO
            if resultado:
                print("====================================================")
                print("Código:", resultado["codigo"])
                print("Nombre:", resultado["nombre"])
                print("Plataforma:", resultado["plataforma"])
                print("Cantidad:", resultado["cantidad"])
                print("Precio:", resultado["precio"])
                print("====================================================")

            # SINO ENCUENTRA NADA IMPRIME OTRO MENSAJE
            else:
                print("No hay videojuegos registrados con ese codigo")

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

    # GENERACION DE REPORTE JSON
    elif opcion == 5:
        # VALIDAMOS QUE HAYAN OBJETOS GUARDADOS EN EL INVENTARIO
        if len(inventario) == 0:
            print("Inventario no existente")

        # SI EL INVENTARIO EXISTE ENTONCES SE GENERA EL REPORTE
        else:
            print("Generando reporte...")
            # SE CREA EL REPORTE
            with open("inventario.json", "w") as archivo:
                json.dump(inventario, archivo, indent=4)
            print(f"Reporte generado correctamente. Se exportaron {len(inventario)} videojuegos.")
            print("Archivo creado: inventario.json")

    # EN ESTE BLOQUE SE SALE DEL INVENTARIO
    elif opcion == 6:
        print("Saliendo del inventario... Hasta pronto!!!!")
        break
