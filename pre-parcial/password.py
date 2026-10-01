password = "5678"
intentos = 1
password_usuario = ""

while password != password_usuario and intentos <= 3:
    print(f"Tienes {intentos} de 3 intentos.")
    password_usuario = input("Por favor ingrese su contrasenia: \n")
    intentos += 1

print("Intentos ", intentos)
if intentos > 3:
    print("Ha superado el limite de intentos ")
else:
    print("Contrasenia correcta")
