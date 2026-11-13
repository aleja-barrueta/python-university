contactos = {"Laura": "3104567890", "Pedro": "3209876543", "Sofia": "3001122334"}
decision_usuario = 0

while decision_usuario != 3:
    decision_usuario = int(
        input(
            "Indique que accion desea realizar: 1 Ver todos los contactos, 2 Crear o editar contacto, 3 Salir."
        )
    )

    if decision_usuario == 1:
        for (
            key,
            value,
        ) in (
            contactos.items()
        ):  # key,value son los elementos dentro del diccionario. E items como funcion simboliza los elementos del diccionario.
            print(key, value)

    if decision_usuario == 2:
        buscar_contacto = input("Ingrese el nombre del contacto: \n")
        if buscar_contacto in contactos:
            modificar_contacto = input(
                "Se actualizara el telefono, por favor ingresa el nuevo telefono: \n"
            )
            contactos[buscar_contacto] = modificar_contacto
        else:
            agregar_contacto = input("Contacto nuevo, ingresa el telefono: \n")
            contactos[buscar_contacto] = agregar_contacto
    if decision_usuario == 3:
        print("Gracias por acceder a directorio telefonico. Adios")
