palabras = ["hola", "adios", "oki"]
palabras_copy = palabras.copy()
palabras_invertidas = []
for palabra in palabras:
    palabras_invertidas.append(palabras_copy.pop())
print(f"La lista de palabras invertidas es: {palabras_invertidas}")
