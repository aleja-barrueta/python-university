hasta = int(input("Por favor, ingrese su edad \n"))
contador_anios = 0
print("Usted ha cumplido: ", end="")
for edad in range(hasta):
    print(edad + 1, end=", ")
