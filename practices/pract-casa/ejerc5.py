lista1 = [1, 5, 7, 8, 3, 4]
lista2 = [4, 5, 6, 7, 9, 1]
lista_combinada = []

for num in lista1:
    if num not in lista_combinada:
        lista_combinada.append(num)

for num in lista2:
    if num not in lista_combinada:
        lista_combinada.append(num)
lista_combinada.sort(reverse=False)

print(f"Lista combinada es:  {lista_combinada}")
