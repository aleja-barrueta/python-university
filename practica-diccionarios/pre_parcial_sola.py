#crear un sistema para registrar estudiantes, los estudiantes deben tener, documento de identidad, nombre, y edad..
#almacenar los datos de forma dinamica en un diccionario y utilizar funciones.

casa = {}
casa["sala"]= {"mueble": 2, "comedor": 1, "alfombra": 1}
casa["cocina"]= {"nevera": 1, "vasos": 2, "platos": 2, "cucharas": 5, "tenedores": 3}
print(f"En casa hay {casa["sala"]["mueble"]} muebles")
#estudiantes["123"]= {"nombre": "andres", "edad": 19}
#estudiantes["1234"]= {"nombre": "maria", "edad": 19}

def modificar_estudiante( documento, nombre, edad):
    estudiantes[documento]={"nombre": nombre, "edad": edad}

estudiantes= {}
menu= input("Bienvenido al sistema Estudiantes, seleccione que accion desea realizar. \n1- Consultar estudiantes\n2- Registrar estudiante\n3- Modificar estudiante\n4- Buscar por nombre\n5-Salir\n")

while menu != "5":
    if menu == "1":
        print("Los estudiantes son:")
        print(estudiantes)
    if menu == "2":
        documento_estudiante= input("Ingrese el numero de documento:\n")
        nombre_estudiante= input("Ingrese el nombre:\n")
        edad_estudiante= input("Ingrese edad:\n")
        modificar_estudiante(documento_estudiante, nombre_estudiante, edad_estudiante)
    if menu == "3":
        documento_estudiante= input("Ingrese el numero de documento:\n")
        if documento_estudiante in estudiantes:
            nombre_estudiante= input("Ingrese el nombre:\n")
            edad_estudiante= input("Ingrese edad:\n")
            modificar_estudiante(documento_estudiante, nombre_estudiante, edad_estudiante)
        else:
            print("Estudiante no encontrado")

    if menu == "4":
        nombre_buscar= input("Ingrese el nombre:\n")
        for estudiante in estudiantes.values():
            #estudiantes["1234"]= {"nombre": "maria", "edad": 19}
            #estudiante = estudiantes[documento] #{"nombre": "maria", "edad": 19}
            if nombre_buscar == estudiante["nombre"]:
                print("El estudiante es: ", estudiante)
        
    menu= input("\nBienvenido al sistema Estudiantes, seleccione que accion desea realizar. \n1- Consultar estudiantes\n2- Registrar estudiante\n3- Modificar estudiante\n4- Buscar por nombre\n5-Salir\n")

