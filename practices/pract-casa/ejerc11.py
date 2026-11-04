edades = [3, 18, 5, 35]
edades_copy = edades.copy()

iterador = 0
while iterador < len(edades):
    if edades[iterador] < 18:
        edades_copy.remove(edades[iterador])
    iterador += 1

print(edades_copy)
# for edad in edades:
#     if edad < 18:
#         edades_copy.remove(edad)
