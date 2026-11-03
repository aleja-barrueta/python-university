dias_semana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
dia_usuario = input("Por favor ingrese un dia de la semana: \n")
if dia_usuario in dias_semana:
    print("Dia valido")
else:
    print("Dia invalido")
