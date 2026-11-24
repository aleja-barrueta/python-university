# crear un menu interactivo el cual permita mostrar los estudiantes, modificar, crear, y buscar por numero de documento, nombre, edad, materia.
# el diccionario de estudiantes debe usar el numero de documento como llave, cada estudiante tendra nombre, edad, materia. Usar funciones para no repetir codigo.

estudiantes = {}


def guardar_o_modificar_estudiante(documento, nombre, edad, materia):
    estudiantes[documento] = {"nombre": nombre, "edad": edad, "materia": materia}


def definirEstudiante(estaCreando):
    documento_estudiante = input("Ingrese el documento del estudiante:\n")
    nombre_estudiante = input("Ingrese el nombre del estudiante:\n")
    edad_estudiante = input("Ingrese la edad del estudiante:\n")
    materia_estudiante = input("Ingrese la materia del estudiante:\n")
    if estaCreando:

        guardar_o_modificar_estudiante(
            documento_estudiante,
            nombre_estudiante,
            edad_estudiante,
            materia_estudiante,
        )
        print(estudiantes)
    else:
        if documento_estudiante in estudiantes:
            guardar_o_modificar_estudiante(
                documento_estudiante,
                nombre_estudiante,
                edad_estudiante,
                materia_estudiante,
            )
            print(estudiantes)
        else:
            print("El documeto no se encuentra registrado.")


menu = input(
    "Ingrese la funcion que desea realizar\n1-Crear\n2-Modificar\n3-Buscar por numero de documento\n4-Buscar por nombre\n5-Buscar por edad\n6-Buscar por cualquier parametro del estudiante\n7-Buscar por materia\n8-Salir\n"
)


while menu != "8":
    if menu == "1":
        # documento_estudiante = input("Ingrese el documento del estudiante:\n")
        # nombre_estudiante = input("Ingrese el nombre del estudiante:\n")
        # edad_estudiante = input("Ingrese la edad del estudiante:\n")
        # materia_estudiante = input("Ingrese la materia del estudiante:\n")
        # guardar_o_modificar_estudiante(
        #     documento_estudiante,
        #     nombre_estudiante,
        #     edad_estudiante,
        #     materia_estudiante,
        # )
        # print(estudiantes)
        definirEstudiante(True)

    if menu == "2":
        # documento_buscar = input("Ingrese el documento :\n")
        # if documento_buscar in estudiantes:
        #     nombre_estudiante = input("Ingrese el nombre del estudiante:\n")
        #     edad_estudiante = input("Ingrese la edad del estudiante:\n")
        #     materia_estudiante = input("Ingrese la materia del estudiante:\n")
        #     guardar_o_modificar_estudiante(
        #         documento_buscar, nombre_estudiante, edad_estudiante, materia_estudiante
        #     )
        # else:
        #     print("El documeto no se encuentra registrado.")
        definirEstudiante(False)

    if menu == "3":
        documento_buscar = input("Ingrese el documento a buscar:\n")
        if documento_buscar in estudiantes:
            print(f"El estudiante es: {estudiantes[documento_buscar]}")
        else:
            print("El documeto no se encuentra registrado.")

    if menu == "4":
        nombre_buscar = "Ingrese el nombre a buscar:\n"
        for estudiante in estudiantes.values():
            if nombre_buscar == estudiante["nombre"]:
                print(f"El estudiante es: {estudiante}")
            else:
                print("El nombre no se encuentra registrado.")

    if menu == "5":
        buscar_edad = input("Ingrese la edad del estudiante")
        for estudiante in estudiantes.values():
            if buscar_edad == estudiante["edad"]:
                print(f"El estudiante es: {estudiante}")
            else:
                print("No hay estudiantes con esa edad.")

    if menu == "6":
        parametros = ["documento", "edad", "nombre", "materia"]
        opcion = input(
            "Ingrese la opcion por la cual va a consultar: documento | nombre | edad | materia:\n"
        )
        if opcion in parametros and len(estudiantes) > 0:
            if opcion == "documento":
                documento = input("Ingrese el documento:\n")
                if documento in estudiantes:
                    print(f"El estudiante es: {estudiantes[documento]}")
                else:
                    print("El documeto no se encuentra registrado.")
            if opcion == "nombre":
                nombre = input("Ingrese el nombre a buscar:\n")
                for estudiante in estudiantes.values():
                    if nombre == estudiante["nombre"]:
                        print(f"El estudiante es: {estudiante}")
                    else:
                        print("El nombre no se encuentra registrado.")
            if opcion == "edad":
                edad = input("Ingrese la edad del estudiante")
                for estudiante in estudiantes.values():
                    if edad == estudiante["edad"]:
                        print(f"El estudiante es: {estudiante}")
                    else:
                        print("No hay estudiantes con esa edad.")
            if opcion == "materia":
                materia = input("Ingrese la materia del estudiante")
                for estudiante in estudiantes.values():
                    if materia == estudiante["materia"]:
                        print(f"El estudiante es: {estudiante}")
                    else:
                        print("No hay estudiantes con esa materia.")
        else:
            print("Campo no valido")

    menu = input(
        "\nIngrese la funcion que desea realizar\n1-Crear\n2-Modificar\n3-Buscar por numero de documento\n4-Buscar por nombre\n5-Buscar por edad\n6-Buscar por cualquier parametro del estudiante\n7-Buscar por materia\n8-Salir\n"
    )
