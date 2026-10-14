lista_de_numeros = []  # lista vacia
for numero in range(11):  # rango hasta donde quiero mi lista
    if numero > 0:  # para que mi lista inicie en un numero diferente de 0.
        lista_de_numeros.append(
            numero
        )  # mi lista con la cantidad de elementos que indique en el rango.

acumulador = 0  # va a iniciar su recorrido desde el indice 0, e ira sumando de 1 en 1
while acumulador < len(
    lista_de_numeros
):  # condicion mi indice debe ser menor que la cantidad de elementos
    # le colocamos len porque este contara los elementos de la lista, nos devuelve un numero
    # y asi podemos comparar enteros con enteros de: acumulador y lista_de_numeros
    print(
        f"El numero {lista_de_numeros[acumulador]} esta ubicado en la posicion {acumulador}"
    )
    acumulador += 1  # aqui se le asigna +1 para que vaya sumando los que ya ha acumulado.
    

for num in lista_de_numeros: 
    if num % 2 == 0:
        lista_de_numeros.remove(num)

print(f"Los numeros pares han sido eliminados, su lista queda asi: {lista_de_numeros}")

