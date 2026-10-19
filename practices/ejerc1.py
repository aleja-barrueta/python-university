numeros = []
contador = 0
for num in range(10):
    numeros.append(num)
while contador < num:
    print(numeros)
    contador += 1
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)

print("Su lista de numeros retirando los pares queda asi: ", numeros)
