# crear un menu interactivo el cual permita mostrar los estudiantes, modificar, crear, y buscar por numero de documento, nombre, edad, materia.
# el diccionario de estudiantes debe usar el numero de documento como llave, cada estudiante tendra nombre, edad, materia. Usar funciones para no repetir codigo.

estudiantes = {}


def crear_o_editar_estudiante(documento, nombre, apellido, edad, materia):
    estudiantes[documento] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "materia": materia,
    }


def crear_estudiante():
    documento_estudiante = input("Ingrese el documento del estudiante:\n")
    nombre_estudiante = input("Ingrese el nombre del estudiante:\n")
    apellido_estudiante = input("Ingrese el apellido del estudiante:\n")
    edad_estudiante = input("Ingrese la edad del estudiante:\n")
    materia_estudiante = input("Ingrese la materia del estudiante:\n")
    crear_o_editar_estudiante(
        documento_estudiante,
        nombre_estudiante,
        apellido_estudiante,
        edad_estudiante,
        materia_estudiante,
    )
    mostrar_estudiantes()


def mostrar_estudiantes():
    print(estudiantes)


def modificar_estudiante():
    buscar_estudiante = input(
        "Ingrese el documento del estudiante que desea modificar:\n"
    )
    if buscar_estudiante in estudiantes:
        nombre_estudiante = input("Ingrese el nombre del estudiante:\n")
        apellido_estudiante = input("Ingrese el apellido del estudiante:\n")
        edad_estudiante = input("Ingrese la edad del estudiante:\n")
        materia_estudiante = input("Ingrese la materia del estudiante:\n")
        crear_o_editar_estudiante(
            buscar_estudiante,
            nombre_estudiante,
            apellido_estudiante,
            edad_estudiante,
            materia_estudiante,
        )
        mostrar_estudiantes()
    else:
        print("Estudiante no encontrado")


def buscar_por_documento():
    documento_buscar = input("Ingrese el numero de documento\n")
    if documento_buscar in estudiantes:
        print(f"El estudiante es: {estudiantes[documento_buscar]}")
    else:
        print("Estudiante no encontrado")


def buscar_por_nombre():
    buscar_nombre = input("Ingrese el nombre del estudiante:\n")
    for estudiante in estudiantes.values():
        if buscar_nombre == estudiante["nombre"]:
            print(f"El estudiante es: {estudiante}")
        else:
            print("Estudiante no encontrado")


def buscar_por_edad():
    buscar_edad = input("Ingrese la edad del estudiante:\n")
    for estudiante in estudiantes.values():
        if buscar_edad == estudiante["edad"]:
            print(f"El estudiante es: {estudiante}")
        else:
            print("Estudiante no encontrado")


def buscar_por_materia():
    buscar_materia = input("Ingrese la materia del estudiante:\n")
    for estudiante in estudiantes.values():
        if buscar_materia == estudiante["materia"]:
            print(f"El estudiante es: {estudiante}")
        else:
            print("Estudiante no encontrado")


mensaje_menu = "\nIngrese la opcion que desea realizar\n0-Mostrar estudiantes\n1- Crear\n2-Modificar\n3-Buscar por numero de documento\n4-Buscar por nombre\n5-Buscar por edad\n6-Buscar por materia\n7-Salir:\n"
menu = input(mensaje_menu)

while menu != "7":
    if menu == "0":
        mostrar_estudiantes()
    elif menu == "1":
        crear_estudiante()
    elif menu == "2":
        modificar_estudiante()
    elif menu == "3":
        buscar_por_documento()
    elif menu == "4":
        buscar_por_nombre()
    elif menu == "5":
        buscar_por_edad()
    elif menu == "6":
        buscar_por_materia()
    elif menu == "7":
        print("Bye.")
    else:
        print("\nOpcion no validad, intentalo de nuevo!!!")

    menu = input(mensaje_menu)
