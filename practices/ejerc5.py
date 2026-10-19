lista1 = [1, 6, 9, 7, 5]
lista2 = [10, 9, 0, 8, 5]
lista_combinada = []

for num in lista1:
    if num not in lista_combinada:
        lista_combinada.append(num)
for num in lista2:
    if num not in lista_combinada:
        lista_combinada.append(num)

lista_combinada.sort(reverse=False)
print("La lista combinada es= ", lista_combinada)
