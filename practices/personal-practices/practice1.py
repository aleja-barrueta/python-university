edades = [11, 34, 5, 7, 89, 18, 20]
copia_edades = edades.copy()
iterador = 0
while iterador < len(edades):
    if edades[iterador] < 18:
        copia_edades.remove(edades[iterador])
    iterador += 1

print("Mayores de edad :", copia_edades)
