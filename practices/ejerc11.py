edades = [25, 16, 27, 2, 10, 34]
edades_copy = edades.copy()  # [25, 16, 27, 2, 10, 34]

indices = 0
while indices < len(edades):
    if edades[indices] < 18:
        edades_copy.remove(edades[indices])
    indices += 1

print(f"La lista sin menores de edad es: {edades_copy}")
