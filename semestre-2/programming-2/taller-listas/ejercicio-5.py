from turtle import left

lista_uno = [2, 1, 7, 9, 8, 8, 9]  # ambas listas solicitadas
lista_dos = [5, 3, 9, 6, 9, 6, 3]

lista_uno.extend(lista_dos) #

lista_combinada = []

for num in set(lista_uno):
    lista_combinada.append(num)

print(
    f"La lista combinada sin elementos duplicados con las dos listas anteriores es: {lista_combinada}"
)

# # for num in lista_uno:
# #     lista_combinada.append(num)

# # print(f"Lista 1 agregada a la lista combinada: {lista_combinada}")

# # for num in lista_dos:
# #     lista_combinada.append(num)

# # print(f"La lista combinada de los dos listas anteriores son: {lista_combinada}")

# lista_uno.extend(lista_dos)

# lista_combinada = list(set(lista_uno))
# print(
#     f"La lista combinada sin elementos duplicados con las dos listas anteriores es: {lista_combinada}"
# )
