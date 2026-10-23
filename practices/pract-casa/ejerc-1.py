# pedirle al usuario que adivine una palabra usando el ciclo while
# cuando la palabra sea adivinada debera mostrarle al usuario
# acertaste

# print("Bienvenido al juego: Adivina la Palabra")
# # paso1 declarar una variable que se actualice
# palabra_usuario = input("Por favor ingresa la palabra con la que desees participar \n")
# palabra_acertada = "adios"
# # paso2 creo una condicion usando mi variable de control para que el ciclo no sea infinito
# while palabra_usuario != palabra_acertada:
#     # paso 3 refresco y actualizo mi variable para volver a compararla a ver si cumple con mi condicion
#     palabra_usuario = input(
#         "Lo sentimos, la palabra es incorrecta :(! \n No te rindas, vuelve a intentarlo :)! \n "
#     )
# print("Felicidades, acertaste la palabra! :) ")

# solicitar al usuario mediante un ciclo while que llene una lista hasta que el  usuario diga NO, y al final imprime la lista.
# lista = []
# elemento_lista = input("Por favor ingrese la palabra que desea ingresar a la lista: \n")
# stop = "NO"
# while elemento_lista != stop:
#     lista.append(elemento_lista)
#     elemento_lista = input(
#         "Palabra agregada, si deseas continuar indica otra palabra, de lo contrario escribe: NO: \n"
#     )
# print(f"Los elementos fueron integrados a la lista, tu lista es: {lista}")


# declara una lista con los nros del 1 al 10 recorrer la lista usando el ciclo while, sumar todos los elementos de la lista y que me muestre el total de la suma.
# lista = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0]
# lista_copy = lista.copy()
# incrementador = 0
# print(f"My list: {lista}")
# while incrementador < len(lista):
#     if lista[incrementador] == 0:
#         lista_copy.remove(lista[incrementador])
#     incrementador += 1
# print(f"La lista modificada es: {lista_copy}")

# llenar una lista con frutas con las que ingrese el usuario, despues usa el bucle while recorrer la lista y reemplazar o actualizar la fruta "banana" que debe estar incluido en la lista inicial por la fruta "kiwi"
lista_frutas = ["banana"]
print("Su lista inicial es: ", lista_frutas)
parada = "NO"  # variable para comparar con mi variable de control
frutas_usuario = input(
    "Por favor indique el nombre de la fruta que desea agregar a la lista, si no quiere agregar ninguna indique NO: \n"
)  # variable de control
while frutas_usuario != parada:
    lista_frutas.append(frutas_usuario)
    frutas_usuario = input(
        "Por favor indique el nombre de la fruta que desea agregar a la lista, si no quiere agregar ninguna indique NO: \n"
    )
print(lista_frutas)
