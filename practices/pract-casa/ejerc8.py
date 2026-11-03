lista_a = [1, 4, 5, 6, 8, 3, 2, 1, 5]
lista_b = [7, 5, 4, 3, 2, 1, 5, 5]
lista_comun = []
for num in lista_a:
    if num in lista_b and num not in lista_comun:
        lista_comun.append(num)
print(f"La lista comun es {lista_comun}")
