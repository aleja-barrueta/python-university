frutas = ["manzana", "banana", "naranja", "uva"]
fruta_usuario = input("Por favor, ingresa una fruta: \n")
for fruta in frutas:
    if fruta == fruta_usuario:
        fruta_index = frutas.index(fruta)
        frutas[fruta_index] = "kiwi"
print(f"Su lista es {frutas}")
