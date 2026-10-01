limite = int(input("Cuantos numeros desea introducir \n"))
contador_par = 0
contador_impar = 0
for indice in range(limite):
    print("Ingrese el numero en posicion ", indice + 1)
    ingresado = int(input())
    if ingresado % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1
print(f"La cantidad de numeros par es de  {contador_par}")
print(f"La cantidad de numeros impares es de: {contador_impar}")
