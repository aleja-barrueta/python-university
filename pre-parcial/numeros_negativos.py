limite = int(
    input("Indique cuantos numeros desea intoducir: ")
)  # aqui definimos cuantas veces se va apedir que ingrese un numero
cant_negativos = 0  # aqui inicia el conteo de numeros negativos, desde 0.
for indice in range(limite):  # aqui indicamos las veces que va a iterar
    print(
        "Ingrese el numero en la posicion: ", indice + 1
    )  # le mostramos al usuario en que posicion va ir colocando los nros que ingrese, estetico
    num_ingresado = int(input())  # el numero que ingresa el usuario
    if num_ingresado < 0:  # la condicion para determinar si es negativo
        cant_negativos += 1  # contador o acumulador en el cual se va actualizando con la suma de cada nro negativo entrante
print(f"Usted tiene {cant_negativos} numeros negativos.")
