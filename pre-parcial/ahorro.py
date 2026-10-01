# ahorro
ahorro = float(
    input("Ingrese la cantidad que desee ahorrar: \n")
)  # declaro la variable, dependera del monto que el usuario desee ahorrar
cantidad = 0  # declaro la variable cantidad, que es 0 porque en  0 inicia el ahorro
while cantidad <= ahorro:  # condicion para el bucle y que este no sea infinito
    cantidad += float(
        input("Ingrese la cantidad a ahorrar \n")
    )  # aqui el usuario ingresa la cantidad de dinero que
    # desee ahorrar, y el lo va sumando hasta cumplir con la condicion del ciclo;
