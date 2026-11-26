# crear un menu interactivo el cual permita mostrar los estudiantes, modificar, crear, y buscar por numero de documento, nombre, edad, materia, y eliminar al estudiante.
# el diccionario de estudiantes debe usar el numero de documento como llave, cada estudiante tendra nombre, edad, materia. Usar funciones para no repetir codigo.

estudiantes = {}


def crear_o_modificar_estudiantes(documento, nombre, edad, materia):
    estudiantes[documento] = {"nombre": nombre, "edad": edad, "materia": materia}


def crear_estudiante():
    documento_estudiante = input("Por favor ingrese el documento del estudiante:\n")
    nombre_estudiante = input("Por favor ingrese el nombre del estudiante:\n")
    edad_estudiante = input("Por favor ingrese la edad del estudiante:\n")
    materia_estudiante = input("Por favor ingrese la materia del estudiante:\n")
    crear_o_modificar_estudiantes(
        documento_estudiante, nombre_estudiante, edad_estudiante, materia_estudiante
    )


def modificar_estudiante():
    documento_buscar = input(
        "Ingrese el documento del estudiante que desea modificar:\n"
    )
    if documento_buscar in estudiantes:
        decision_usuario = input(
            "Indique que accion desea realizar\n1-Cambiar el nombre\n2-Cambiar edad\n3-Cambiar materia\n4-salir\n"
        )
        if decision_usuario == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre:\n")
            estudiantes[documento_buscar]["nombre"] = nuevo_nombre
            print(f"El cambio ha sido realizado {estudiantes[documento_buscar]}")
        elif decision_usuario == "2":
            edad_nueva = input("Ingrese nueva edad:\n")
            estudiantes[documento_buscar]["edad"] = edad_nueva
            print(f"El cambio ha sido realizado {estudiantes[documento_buscar]}")
        elif decision_usuario == "3":
            materia_nueva = input("Ingrese la nueva materia:\n")
            estudiantes[documento_buscar]["materia"] = materia_nueva
            print(f"El cambio ha sido realizado {estudiantes[documento_buscar]}")
        else:
            print("Se cancelo la operacion a realizar:\n")
    else:
        print("El estudiante no se encuentra registrado.")


def buscar_por_documento():
    documento_buscar = input("Ingrese el numero del documento que desea buscar:\n")
    if documento_buscar in estudiantes:
        print(f"El estudiante es: {estudiantes[documento_buscar]}")
    else:
        print("El estudiante no se encuentra registrado")


def buscar_por_nombre():
    nombre_buscar = input("Ingrese el numero del documento que desea buscar:\n")
    for estudiante in estudiantes:
        if nombre_buscar == estudiante["nombre"]:
            print(f"El estudiante es: {estudiante}")
        else:
            print("El estudiante no se encuentra registrado")


def eliminar_estudiante():
    documento_buscar = input(
        "Ingrese el documento del estudiante que desea eliminar:\n"
    )
    if documento_buscar in estudiantes:
        estudiantes.pop(documento_buscar)
        print("El estudiante ha sido eliminado")
    else:
        print("El estudiante no se encuentra registrado")


menu = input(
    "Indique que accion desea realizar\n0-Consultar\n1-Crear\n2-Modificar\n3-Buscar por numero de documento\n4-Buscar por nombre\n5-Buscar por edad\n6-Buscar por materia\n7-Eliminar estudiante\n8-Salir\n"
)

while menu != "8":
    if menu == "0":
        print(estudiantes)

    if menu == "1":
        crear_estudiante()

    if menu == "2":
        modificar_estudiante()

    if menu == "3":
        buscar_por_documento()

    if menu == "4":
        buscar_por_nombre()

    if menu == "7":
        eliminar_estudiante()

    menu = input(
        "Indique que accion desea realizar\n0-Consultar\n1-Crear\n2-Modificar\n3-Buscar por numero de documento\n4-Buscar por nombre\5-Buscar por edad\n6-Buscar por materia\n7-Eliminar estudiante\n8-Salir\n"
    )
