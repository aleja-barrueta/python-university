# ahorro
ahorro = float(
    input("Ingrese la cantidad que desee ahorrar: \n")
)  # declaro la variable, dependera del monto que el usuario desee ahorrar
cantidad = 0  # declaro la variable cantidad, que es 0 porque en  0 inicia el ahorro
while cantidad <= ahorro:  # condicion para el bucle y que este no sea infinito
    valor = float(
        (input("Ingrese la cantidad a ahorrar \n"))
    )  # aqui el usuario ingresa la cantidad de dinero que
    # desee ahorrar, y el lo va sumando hasta cumplir con la condicion del ciclo;
    if valor > 0:  # conidicion para evitar numeros negativos
        cantidad += valor  # aqui comienza el ciclo segun los montos que ingrese el
        # usuario para llevar la cuenta de lo que ha ahorrado cumplir con
        # el ciclo y ahi mismo saber donde parar
        print("El ahorro que usted lleva es de: ", cantidad)  # le mostramos al
        # usuario la suma de lo que ha ido ahorrando
    else:
        print("por favor ingrese una cantidad mayor a 0")