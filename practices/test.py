# crear dos listas de numeros que contengan duplicados, en una nueva lista poner los elementos duplicados que se repiten en ambas listas

lista_uno = [1, 2, 2, 4, 5, 6, 6]
lista_dos = [3, 5, 6, 7, 8, 1]
lista_tres = [3, 5, 2, 7, 8, 1]
nueva_lista = [] # 1, 5
for num in lista_uno:
    if num in lista_dos and num in lista_tres and num not in nueva_lista:
        nueva_lista.append(num)

print(nueva_lista)

