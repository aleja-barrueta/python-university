# # ejemplo1
# Estudiantes = ["Carlos", "Luisa", "Franklin"]
# print(Estudiantes)


# # ejemplo2
# lista_compras = ["Harina", "Arroz", "Huevos", "Aceite"]
# print(lista_compras[0], ", ", lista_compras[2])


# # ejemplo3 append adjunta a la lista un elemento nuevo
# lista_compras = ["Harina", "Arroz", "Huevos", "Aceite"]
# lista_compras.append("Carne")
# print(lista_compras)


# # ejemplo 3 extend añadir lista 1 a lista 2
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista1.extend(lista2)
# print(lista1)


# # ejemplo 4 metodo insert
# lista_compras.insert(2, "leche")
# print(lista_compras)


# # ejemplo5 metodo pop
# lista_compras.insert(2, "leche")
# lista_compras.pop(3)
# print(lista_compras)


# # ejemplo6 remove
# lista_compras.insert(2, "leche")
# lista_compras.pop(3)
# lista_compras.remove("Aceite")
# print(lista_compras)

#ejemplo funcion tupla
andres = ("hola", "chao")
saludo = andres.count("hola") #muestra en que indice se ubica el hola
index_item = andres.index("hola") #cuenta cuantos hola hay.
print("posicion del elemeto buscado", index_item)
print("total de saludos ", saludo)
