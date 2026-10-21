lista_a = [1, 9, 3, 4, 6, 8, 8]
lista_b = [5, 6, 7, 8, 9]
lista_comun = []  # 9, 6, 8

for num in lista_a:
    if num in lista_b and num not in lista_comun:
        lista_comun.append(num)

print(f"lista es: {lista_comun}")
