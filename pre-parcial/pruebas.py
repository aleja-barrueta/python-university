# prueba = ("face", "hair", "body", "nails")
# # fragmento = slice(3)
# test = prueba[slice(3)]
# print(test)
# test = prueba[:2]

# print(test)


# my_dict = {"chocolate": 5, "naranja": 3}
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(f"La cantidad de chocolate que hay es de: { my_dict["chocolate"]}")
# print()
# print("Iterando my dict")
# for i in my_dict.keys():
#     print(f"my key is: {i}")

# for i in my_dict.values():
#     print(f"my value is: {i}")

# print()
# for item in my_dict.items():
#     print(f"my item is: {item}")

# print("\t\t\t\t\t\tBienvenido al inventario de Aleja")
# stop = "si"
# inventario = {}
# while stop.lower() == "si":
#     item = input("Ingrese el nombre del articulo: \n")
#     cantidad = int(input("Ingrese la catidad del articulo: \n"))
#     if item in inventario:
#         inventario[item] = inventario[item] + cantidad
#     else:
#         inventario[item] = cantidad

#     stop = input("Desea agregar mas articulos al inventario Si/No: \n")

# print("Su inventario es el siguiente: ")
# for item in inventario.items():
#     print(item)

# imprirmir todos los productos que terminan con la letra a
products = ["naranja", "papaya", "sandia", "melon"]
print(f"La lista de frutas es: {products}")
letra_a_buscar = input("ingrese la letra que desea buscar en la cadena de text: \n")
contador = 0
for product in products:
    # print(f"La letra a buscar es: {letra_a_buscar} en el product: {product}")
    if letra_a_buscar in product:
        contador += 1
        print(f"El producto es: {product}")
    print()
if contador == 0:
    print("No se encontro ninguna letra en la lista de frutas")

contador = 0
letra_a_buscar = input(
    "ingrese la letra que desea buscar al principio en la cadena de text: \n"
)

for product in products:
    # print(f"La letra a buscar es: {letra_a_buscar} en el product: {product}")
    if letra_a_buscar == product[0]:
        contador += 1
        print(f"El producto es: {product}")
    print()

if contador == 0:
    print("No se encontro ninguna letra al principio en la lista de frutas")

contador = 0
letra_a_buscar = input(
    "ingrese la letra que desea buscar al final en la cadena de text: \n"
)

for product in products:
    # print(f"La letra a buscar es: {letra_a_buscar} en el product: {product}")
    if letra_a_buscar == product[-1]:
        contador += 1
        print(f"El producto es: {product}")
    print()

if contador == 0:
    print("No se encontro ninguna letra al final en la lista de frutas")
