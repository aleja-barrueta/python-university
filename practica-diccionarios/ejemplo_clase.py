#crear un sistema para registrar estudiantes, los estudiantes deben tener, documento de identidad, nombre y edad. Almacenar los datos de forma dinamica en un diccionario y utilizar al menos dos funciones
estudiantes = {}
def registrar_estudiante(doc,nom,edad):
    estudiantes[doc] ={"nombre":nom, "edad":edad}
    print("Estudiante registrado con exito!")
def consultar_estudiante():
    print(estudiantes)

menu = input("Ingrese una opción: 1 - registrar, 2 - consultar, 3 - Buscar por nombre, 4 - modificar, 5 - eliminar, 6 - salir :")
while menu != "6":
    if menu == "1":
        documento_estudiante = input("Ingrese el documento del estudiante a registrar: ")
        nombre_estudiante = input("Ingrese el nombre del estudiante a registrar: ")
        edad_estudiante = input("Ingrese la edad del estudiante a registrar: ")
        registrar_estudiante(documento_estudiante,nombre_estudiante,edad_estudiante)
    elif menu == "2":
        consultar_estudiante()
    elif menu == "3":
        nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
        dato_encontrado = False
        for documento in estudiantes:
            if estudiantes[documento]["nombre"] == nombre_buscar:
                dato_encontrado = True
                print("Estudiante Encontrado: Documento: ",documento," Nombre: ",nombre_buscar," Edad: ",estudiantes[documento]["edad"])
        if dato_encontrado == False:
            print("No se encontro el estudiante!")
    elif menu == "4":
        documento_buscar = input("Ingrese el documento del estudiante a modificar: ")
        if documento_buscar in estudiantes:
            opcion_actualizar = input("Estudiante Encontrado! que desea actualizar: 1 - nombre, 2 - edad, 3 - cancelar")
            if opcion_actualizar == "1":
                nombre_actualizar = input("Ingrese el nuevo nombre del estudiante: ")
                estudiantes[documento_estudiante]["nombre"] = nombre_actualizar
                print("Nombre actualizado correctamente!")
            elif opcion_actualizar == "2":
                edad_actualizar = input("Ingrese la nueva edad del estudiante: ")
                estudiantes[documento_estudiante]["edad"] = edad_actualizar
                print("Edad actualizada correctamente!")
            else:
                print("Se cancelo la operación de actualizar!")
    else:
        documento_eliminar = input("Ingrese el documento del estudiante a eliminar: ")
        if documento_eliminar in estudiantes:
            estudiantes.pop(documento_eliminar)
            print("Se elimino correctamente!")
        else:
            print("No se encontro el estudiante!")
    menu = input("Ingrese una opción: 1 - registrar, 2 - consultar, 3 - Buscar por nombre, 4 - modificar, 5 - eliminar, 6 - salir :")

