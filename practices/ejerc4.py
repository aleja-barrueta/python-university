numeros = [1, 2, 4, 4, 5, 9, 0, 1, 7, 4, 7]
contador = 0
buscar = int(input("Por favor ingrese un numero menor a 10 \n"))
if buscar >= 10:
    print("Numero no valido")
for numero in numeros: 
    if buscar == numero:
        contador += 1 
print(f"El numero aparece {contador} veces en la lista.")
    

