print(
    "********* \t\t\t\tBienvenido al Sistema de Gestion de Inventarios \t\t\t*********\n"
)
print(
    "**************************************************************************************************************************\n\n"
)
accion_usuario = 0  # variable que controla el ciclo while y no tengamos un bucle infinito, condicion de parada con el numero 6
inventario_papeleria = ["lapiz", "borrador", "sacapuntas", "hoja"]

while accion_usuario != 6:
    accion_usuario = int(
        input(
            "\nPor favor, indica que accion deseas realizar en el inventario: 1 Mostrar, 2 Agregar, 3 Buscar, 4 Modificar, 5 Eliminar, 6 Salir \n"
        )
    )
    # consultar inventario
    if accion_usuario == 1:
        print(f"Tu inventario es: {inventario_papeleria}")
    # agregar un elemento al inventario
    if accion_usuario == 2:
        producto_agregar = input("Indique el producto que desea agregar: \n")
        inventario_papeleria.append(producto_agregar)
        print(
            f"Se agrego el producto al inventario.\nSu inventario es: {inventario_papeleria}"
        )
    # buscar si un producto esta en la lista y en que indice se encuentra
    if accion_usuario == 3:
        producto_a_buscar = input("Indique cual producto esta buscando: \n")
        if producto_a_buscar in inventario_papeleria:
            indice_producto = inventario_papeleria.index(producto_a_buscar)
            print(f"El producto esta en la lista, su posicion es: {indice_producto}")
        else:
            print("El producto no se encuentra en el inventario.")
    # modificar nombre de un producto existente
    if accion_usuario == 4:
        producto_a_buscar = input(
            "Ingrese el nombre del producto que desea cambiar: \n"
        )
        if producto_a_buscar in inventario_papeleria:
            producto_a_cambiar = input(
                "Ingrese el nuevo nombre para actualizar el producto:\n"
            )
            indice_producto = inventario_papeleria.index(producto_a_buscar)
            inventario_papeleria[indice_producto] = producto_a_cambiar
            print(
                f"El producto fue cambiado.\nEl inventario es: {inventario_papeleria}"
            )
        else:
            print("El producto no se encuentra en el inventario.")
    if accion_usuario == 5:

        opcion_usuario = int(
            input(
                "Ingrese 1 si desea eliminar por indice o 2 por nombre de producto: \n"
            )
        )
        if opcion_usuario == 1:
            indice_producto_eliminar = int(input("Ingrese el indice a buscar: \n"))
            # 3                     # 4
            if indice_producto_eliminar < len(inventario_papeleria):
                inventario_papeleria.pop(indice_producto_eliminar)
                print(
                    f"El producto fue eliminado.\nEl inventario es: {inventario_papeleria}"
                )
            else:
                print("El indice no se encuentra en el inventario.")

        elif opcion_usuario == 2:
            producto_a_eliminar = input(
                "Ingrese el nombre de producto para ser eliminado: \n"
            )

            if producto_a_eliminar in inventario_papeleria:
                inventario_papeleria.remove(producto_a_eliminar)
                print(
                    f"El producto fue eliminado.\nEl inventario es: {inventario_papeleria}"
                )
            else:
                print("El producto no se encuentra en el inventario.")
        else:
            print("Opcion no valida!")
