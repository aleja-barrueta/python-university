def clasificar_estatura(estatura):
    if estatura >= 140 and estatura < 150:
        print("Estatura baja")
    elif estatura >= 150 and estatura < 160:
        print("Estatura medio")
    elif estatura >= 160 and estatura < 180:
        print("Estatura alta")
    else:
        print("Estatura fuera de los rangos")


clasificar_estatura(200)
