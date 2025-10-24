agenda = {("lunes","12:00"): "partido", ("martes","13:00"):"juntada"}
dia = input("Ingrese el dia de la semana ")
hora = input("Ingrese la hora ")
tupla_dia_hora = (dia,hora)
if tupla_dia_hora in agenda:
    print(agenda[tupla_dia_hora])
else:
    print("No hay nada en ese dia/hora")