# contando elementos
numeros = [9, 4, 9]  # variable que voy a comparar con mi variable de control
num_usuario = int(
    input("Por favor ingrese un numero menor a 10 \n")
)  # variable que voy a comparar con los elementos de mi lista inicial.
iterador = 0  # variable de control
contador = 0  # mi variable que cuenta
while iterador < len(numeros):
    num = numeros[iterador]
    if num == num_usuario:
        contador += 1
    iterador += 1
print(f"Su numero se repite {contador} veces en la lista")
