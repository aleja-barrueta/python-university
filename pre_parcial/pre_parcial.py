#crear un sistema para registrar estudiantes, los estudiantes deben tener, documento de identidad, nombre, y edad..
#almacenar los datos de forma dinamica en un diccionario y utilizar funciones.
estudiantes= {}
menu = input("Ingrese una opcion. 1- Registrar, 2- Consultar, 3- Buscar por nombre, 4- Modificar 5- eliminar, 6- salir")
while menu != "6":
    if menu == "1": 
        documento_estudiante= input("Ingrese el documento del estudiante a registrar: ")
        nombre_estudiante= input("Ingrese el nombre del estudiante a registrar: ")
        edad_estudiante= input("Ingrese la edad del estudiante a registrar")
        estudiantes[documento_estudiante]= {"nombre":nombre_estudiante, "edad": edad_estudiante}
    elif menu == "2":
        print(estudiantes)
    elif menu == "3":
        nombre_buscar= input("ingrese el nombre del estudiante a buscar: ")
        dato_encontrado = False
        for documento in estudiantes:
            if estudiantes[documento]["nombre"] == nombre_buscar:
                dato_encontrado= True
                print("Estudiante encontrado: documento: ", documento," nombre : ", nombre_buscar, "edad: ", estudiantes[documento]["edad"])
        if dato_encontrado == False:
            print("No se encontro el estudiante")
    elif menu == "4":
        documento_buscar= input("Ingrese el documento del estudiante a modificar: ")
        if documento_buscar in estudiantes:
            opcion_de_actualizar= input("Estudiante encontrado, que desea actualizar, 1 nombre, 2 edad, 3 cancelar")
            if opcion_de_actualizar == "1":
                    nombre_actualizar= input("Ingrese el nuevo nombre del estudiante: ")
                    estudiantes[documento_estudiante]["nombre"]= nombre_actualizar
                    print("Nombre actualizado correctamente")
            elif opcion_de_actualizar == "2":
                    edad_actualizar= input("Ingrese la nueva edad del estudiante: ")
                    estudiantes[documento_estudiante]["edad"] = edad_actualizar
                    print("Edad actualizada correctamente")
            else:
                    print("Se cancelo la operacion de actualizar")
    else:
        documento_eliminar = input("Ingrese el documento del estudiante a eliminar")
        if documento_eliminar in estudiantes:
              estudiantes.pop(documento_eliminar)
              print("Se elimino correctamente")
        else:
              print("No se encontro")

    menu = input("Ingrese una opcion. 1- Registrar, 2- Consultar, 3- Buscar por nombre, 4- Modificar, 5- eliminar, 6- Salir")


    