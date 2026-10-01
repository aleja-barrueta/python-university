limite = int(input("Indique cuantos numeros desea intoducir: "))
cant_negativos = 0
for indice in range(limite):
    print("Ingrese el numero en la posicion: ", indice + 1)
    num_ingresado = int(input())
    if num_ingresado < 0:
        cant_negativos += 1
print(f"Usted tiene {cant_negativos} numeros negativos.")
