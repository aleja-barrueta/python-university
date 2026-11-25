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


mensaje_menu = "\nIngrese la opcion que desea realizar\n0-Mostrar estudiantes\n1- Crear\n2-Modificar\n3-Buscar por numero de documento\n4-Buscar por nombre\n5-Buscar por edad\n6-Buscar por materia\n7-Salir:\n"
menu = input(mensaje_menu)

while menu != "7":
    if menu == "0":
        print(estudiantes)

    if menu == "1":
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

    if menu == "2":
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
        else:
            print("Estudiante no encontrado")

    if menu == "3":
        documento_buscar = input("Ingrese el numero de documento\n")
        if documento_buscar in estudiantes:
            print(f"El estudiante es: {estudiantes[documento_buscar]}")
        else:
            print("Estudiante no encontrado")

    if menu == "4":
        buscar_nombre = input("Ingrese el nombre del estudiante:\n")
        for estudiante in estudiantes.values():
            if buscar_nombre == estudiante["nombre"]:
                print(f"El estudiante es: {estudiante}")
            else:
                print("Estudiante no encontrado")

    if menu == "5":
        buscar_edad = input("Ingrese la edad del estudiante:\n")
        for estudiante in estudiantes.values():
            if buscar_edad == estudiante["edad"]:
                print(f"El estudiante es: {estudiante}")
            else:
                print("Estudiante no encontrado")

    if menu == "6":
        buscar_materia = input("Ingrese la materia del estudiante:\n")
        for estudiante in estudiantes.values():
            if buscar_materia == estudiante["materia"]:
                print(f"El estudiante es: {estudiante}")
            else:
                print("Estudiante no encontrado")
    menu = input(mensaje_menu)
