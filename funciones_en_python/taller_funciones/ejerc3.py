def sumar_lista(lista):
    sumatoria = 0
    for num in lista:
        sumatoria += num
    return sumatoria


lista_numeros = [
    1,
    2,
    3,
]
resultado = sumar_lista(lista_numeros)

print(f"La sumatoria de la lista de numeros es: {resultado}")
lista_numeros = [1, 2, 3]
