#FUNCION QUE DICE ALGO Y SE USA MUCHAS VECES, NO RETORNA NADA
def saludar(nombre):
    print("Hola, ",nombre)
saludar("David") #LLAMAMOS A LA FUNCION, Y LLENAMOS SU VALOR
saludar("Juana")

#FUNCION QUE RETORNA ALGO
#a vale 30 y b vale 20.5
def sumar(a, b):
    return a + b #variable que almacena el retorno de la funcion
resultado = sumar (30, 20.5)
print("El resultado es: ", resultado)
#si no quiero guardar el resultado en una variable puedo llamarla en un mismo print llamar la funcion y pasarle los parametros
#ejemplo: print(Sumar(20,20)) 40 seria el resultado en consola