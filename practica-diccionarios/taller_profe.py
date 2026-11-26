# crear un sistema para registrar estudiantes, los estudiantes deben tener:
# documento de identidad, nombre y edad. Almacenar los datos de forma dinamica en un diccionario y utilizar al menos dos funciones

estudiantes = {}


def crear_editar_estudiante(documento, nombre, edad):
    estudiantes[documento] = {"nombre": nombre, "edad": edad}


def registrar_estudiante():
    documento_estudiante = input("Ingrese el documento del estudiante:\n")
    nombre_estudiante = input("Ingrese el nombre del estudiante:\n")
    edad_estudiante = input("Ingrese la edad del estudiante:\n")
    crear_editar_estudiante(documento_estudiante, nombre_estudiante, edad_estudiante)


def consultar_estudiante():
    documento_buscar = input("Ingrese el documento del estudiante que desea buscar:\n")
    if documento_buscar in estudiantes:
        print(f"El estudiante es: {estudiantes[documento_buscar]}")
    else:
        print("El estudiante no se encuentra registrado")


def buscar_por_nombre():
    nombre_buscar = input("Ingrese el nombre del estudiante que desea buscar:\n")
    for estudiante in estudiantes.values():
        if nombre_buscar == estudiante["nombre"]:
            print(f"El estudiante es: {estudiante}")
        else:
            print("Estudiante no encontrado")


def modificar_estudiante():
    documento_buscar = input("Ingrese el documento del estudiante que desea buscar:\n")
    if documento_buscar in estudiantes:
        print(f"El estudiante es: {estudiantes[documento_buscar]}")
        decision_usuario = input(
            "Indique que desea cambiar\n1-Nombre\n2Edad\n3-Cancelar\n"
        )
        if decision_usuario == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre:\n")
            estudiantes[documento_buscar]["nombre"] = nuevo_nombre
            print(
                f"El nombre del estudiante ha sido modificado: {estudiantes[documento_buscar]}"
            )
        elif decision_usuario == "2":
            edad_nueva = input("Ingrese la nueva edad del estudiante:\n")
            estudiantes[documento_buscar]["edad"] = edad_nueva
            print(
                f"La edad del estudiante ha sido modificada: {estudiantes[documento_buscar]}"
            )
        elif decision_usuario == "3":
            print("El proceso se ha cancelado")
        else:
            print("Opcion invalida")


def eliminar_estudiante():
    documento_buscar = input("Ingrese el documento del estudiante que desea buscar:\n")
    if documento_buscar in estudiantes:
        estudiantes.pop(documento_buscar)
        print("El estudiante ha sido eliminado")
    else:
        print("El estudiante no se encuentra registrado")


menu = input(
    "Ingrese una opción:\n1-registrar\n2-consultar\n3 - Buscar por nombre\n4 - modificar\n5 - eliminar\n6 - salir:\n"
)

while menu != "6":

    if menu == "1":
        registrar_estudiante()

    if menu == "2":
        consultar_estudiante()

    if menu == "3":
        buscar_por_nombre()

    if menu == "4":
        modificar_estudiante()

    if menu == "5":
        eliminar_estudiante()

    menu = input(
        "Ingrese una opción:\n1-registrar\n2-consultar\n3 - Buscar por nombre\n4 - modificar\n5 - eliminar\n6 - salir:\n"
    )
