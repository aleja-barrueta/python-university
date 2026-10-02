# adivina el numero
secreto = 10
numero = 1
while secreto != numero and numero > 0 and numero <= 20:
    numero = int(input("Ingresa un numero entre 1 hasta 20 para adivinarlo: \n"))
    if numero < secreto:
        print("El numero ingresado es menor al numero a adivinar")
    else:
        print("El numero ingresado es mayor al numero a adivinar")

if  numero > 0 and numero <= 20:
    print("Felicidades, adivinaste el numero secreto")
else:
    print("Ingresaste un numero no permitido.")

#piedra_papel_o_tijera

piedra = "piedra"
papel = "papel"
tijera = "tijera"
jugador = 0
cpu = 0
jugada_cpu = piedra
puntos_a_ganar = 3

while jugador < puntos_a_ganar and cpu < puntos_a_ganar:
    seleccion = input("Escoge piedra, papel o tijera: \n")
    print(f"Escogiste: {seleccion}, CPU: {jugada_cpu}")

    if seleccion == jugada_cpu:
        print("Empatados, no hay puntos para ningun jugador")
        jugada_cpu = papel
    elif (
        (seleccion == piedra and jugada_cpu == tijera)
        or (seleccion == papel and jugada_cpu == piedra)
        or (seleccion == tijera and jugada_cpu == papel)
    ):
        jugador += 1
        print("Has ganado un punto")
    else:
        cpu += 1
        print("CPU gana un punto")
    print(f"Marcador -> Tú: {jugador}, CPU: {cpu} \n")

if jugador == 3:
    print("Ganaste el juego")
else:
    print("Has perdido")


# simulador_inventario
inv_manzanas = 20
while inv_manzanas > 0:
    venta = int(input("Cuantas manzanas deseas llevar: \n"))
    if venta > 20:
        print("Ha ocurrido un error")
        break
    else:
        inv_manzanas -= venta
    print(f"Inventario de manzanas: {inv_manzanas}")
