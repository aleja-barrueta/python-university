lista_num_rep = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6] #lista con numeros repetidos
numero_ingresado = int(input("Por favor ingrese un numero: \n")) #vriable del num que ingresa el usuario
contador = 0 #inicia el conteo en 0

for num in lista_num_rep: #itera la lista inicial 
    if num == numero_ingresado:
        contador += 1

print(f"El numero se ha repetido: {contador}")
