# 1 crear una funcion que sume dos numeros y devuelva el resultado
def sumar(num1, num2):
    return num1 + num2


# 2 crear una funcion que reste dos numeros y devuelva el resultado
def restar(num1, num2):
    return num1 - num2


# 3 crear una funcion que multiplique dos numeros y devuelva el resultado
def multiplicar(num1, num2):
    return num1 * num2


# 4 crear una funcion que divida dos numeros y devuelva el resultado
def dividir(num1, num2):
    return num1 / num2


# 5 usar un bucle while que simule una calculadora
print(
    "Calculadora \nOpcion 1 sumar\nOpcion 2 restar \nOpcion 3 multiplicar \nOpcion 4 dividir \nOpcion 0 si desea salir\n"
)
seleccion_usuario = 1
while seleccion_usuario != 0:
    seleccion_usuario = int(
        input("Por favor seleccione que operacion desea realizar: \n")
    )
    if seleccion_usuario == 1:
        num1 = int(input("Ingrese el primer numero: \n "))
        num2 = int(input("Ingrese el segundo numero: \n "))
        resultado = sumar(num1, num2)
        print("El resultado de la suma es: ", resultado)
    if seleccion_usuario == 2:
        num1 = int(input("Ingrese el primer numero: \n "))
        num2 = int(input("Ingrese el segundo numero: \n "))
        resultado = restar(num1, num2)
        print("El resultado de la resta es: ", resultado)
    if seleccion_usuario == 3:
        num1 = int(input("Ingrese el primer numero: \n "))
        num2 = int(input("Ingrese el segundo numero: \n "))
        resultado = multiplicar(num1, num2)
        print("El resultado de la multiplicacion  es: ", resultado)
    if seleccion_usuario == 4:
        num1 = int(input("Ingrese el primer numero: \n "))
        num2 = int(input("Ingrese el segundo numero: \n "))
        resultado = dividir(num1, num2)
        print("El resultado de la division es: ", resultado)


# y que de la opcion al usuario de realizar una operacion
# 6 el programa debera detenerse cuando el usuario ingrese el numero 0
# 7 cada resultado debera mostrarsele al usuario en pantalla
