# crear un programa en el cual yo pueda registrar las mascotas de los clientes, se van a pedir los siguientes datos:
# numero de identificacion del responsable del animal
# al animal se le van a pedir su raza, color, edad y enfermedad.
# la idea es que pueda registrar, modificar, buscar por numero del documento del dueno, y eliminar el animal.

registro = {}


def registrar_modificar_mascotas(documento, raza, color, edad, enfermedad):
    registro[documento] = {
        "raza": raza,
        "color": color,
        "edad": edad,
        "enfermedad": enfermedad,
    }


def registar_paciente():
    documento_responsable = input(
        "Ingrese el numero de documento del responsable del animal:\n"
    )
    raza_animal = input("Indique la raza del animal:\n")
    color_animal = input("indique el color del animal:\n")
    edad_animal = input("Ingrese la edad del animal:\n")
    enfermedad_animal = input("Ingrese la enfermedad del animal:\n")
    registrar_modificar_mascotas(
        documento_responsable, raza_animal, color_animal, edad_animal, enfermedad_animal
    )


def modificar():
    documento_buscar = input("Ingrese el documento del responsable del animal:\n")
    if documento_buscar in registro:
        seleccion_usuario = input(
            "Indique que desea modificar\n1-Raza\n2-Color\n3-Edad\n4-Enfermedad\n5-Cancelar accion:\n"
        )
        if seleccion_usuario == "1":
            nueva_raza = input("Indique la raza del animal:\n")
            registro[documento_buscar]["raza"] = nueva_raza
            print(f"Se ha modificado correctamente {registro[documento_buscar]}")
        if seleccion_usuario == "2":
            nuevo_color = input("Indique el color del animal:\n")
            registro[documento_buscar]["color"] = nuevo_color
            print(f"Se ha modificado correctamente {registro[documento_buscar]}")
        if seleccion_usuario == "3":
            nueva_edad = input("Indique la edad del animal:\n")
            registro[documento_buscar]["edad"] = nueva_edad
            print(f"Se ha modificado correctamente {registro[documento_buscar]}")
        if seleccion_usuario == "4":
            enfermedad_actualizar = input("Indique la enfermedad del animal:\n")
            registro[documento_buscar]["enfermedad"] = enfermedad_actualizar
            print(f"Se ha modificado correctamente {registro[documento_buscar]}")
        else:
            print("Accion cancelada")
    else:
        print("El documento no se encuentra registrado")


def buscar_por_documento():
    documento_buscar = input("Ingrese el documento:\n")
    if documento_buscar in registro:
        print(f"El animal se encuentra registrado: {registro[documento_buscar]}")
    else:
        print("El animal no se encuentra registrado.")


def eliminar_registro():
    animal_eliminar = input("Ingrese el documento del responsable:\n")
    if animal_eliminar in registro:
        registro.pop(animal_eliminar)
        print("El animal ha sido eliminado")
    else:
        print("El animal no se encuentra registrado")


def mostrar_registros():
    print(registro)


menu = input(
    "\n\nIngrese la accion que desea realizar\n0-Mostrar registros\n1-registrar\n2-modificar\n3-buscar por numero del documento del dueno\n4-eliminar el animal\n5-salir:\n"
)

while menu != "5":
    if menu == "0":
        mostrar_registros()

    if menu == "1":
        registar_paciente()

    if menu == "2":
        modificar()

    if menu == "3":
        buscar_por_documento()

    if menu == "4":
        eliminar_registro()

    menu = input(
        "\n\nIngrese la accion que desea realizar\n0-Mostrar registros\n1-registrar\n2-modificar\n3-buscar por numero del documento del dueno\n4-eliminar el animal\n5-salir:\n"
    )
