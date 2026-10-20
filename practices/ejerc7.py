frutas = ["manzana", "banana", "naranja", "uva"]
fruta_usuario = input("Ingresa una fruta: \n")
for fruit in frutas:
    if fruta_usuario == fruit:
        fruta_index = frutas.index(fruta_usuario)
        frutas.insert(fruta_index, "kiwi")
        frutas.remove(fruta_usuario)
print(frutas)
