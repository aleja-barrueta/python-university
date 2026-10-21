palabras = ["hola", "adios", "hasta", "luego"]
palabras_copy = palabras.copy()
palabras_invertidas = []
for palab in palabras:
    palabras_invertidas.append(palabras_copy.pop())

print(palabras_invertidas)
