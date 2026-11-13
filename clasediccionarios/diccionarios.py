personas = {
    "nombre" : "david",
    "documento" : "123456",  #los documentos se convierten en texto porque NO se operan, todo lo que no se opera es TEXTO "string"
    "telefono" : "5678910",
    "intereses" : ["programacion", "futbol", "juegos"]
}
print(personas["documento"]) #para imprimir solo a documento
print(personas["documento"], personas["intereses"][1], ) #para traer especificamente algo de la lista 


#aplicar SIEMPRE camelCase
#personas es una variable tipo diccionario que tiene varios elementos adentro.
#se imprimen los key escritos exactamente igual que como se escribio al momento de definirlo.


#para cambiarle el valor a un key segun su indice
#personas[intereses][1]= "UFC"

#para crear un nuevo elemento en el diccionario=
personas["ingresos"]= 100

#para reemplazar el nombre de una clave existente en el diccionario
personas ["salario"]= personas.pop("ingresos")
print(personas)

#investigar como recorrer por medio de un for un diccionario. Para luego poder modificar el dato.

