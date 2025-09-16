hemisferio= input("Ingrese su hemisferio(N/S)  ")
mes = int(input("Ingrese el numero del mes en el que se encuentra  " ))
dia = int(input("Ingrese el dia en el que se encuentra  "))
if mes== 12:
    if dia < 21:
        estacion="Primavera"
    else:
        estacion="Verano"
elif mes == 3:
    if dia < 21:
        estacion="Verano"
    else:
        estacion="Otoño"
elif mes == 6:
    if dia < 21:
        estacion="Otoño"
    else:
        estacion="Invierno"
elif mes == 9:
    if dia < 21:
        estacion="Invierno"
    else:
        estacion="Primavera"
    
elif mes < 3:
    estacion="Verano"
elif mes > 3 and mes < 6:
    estacion="Otoño"
elif mes > 6 and mes < 9:
    estacion="Invierno"
elif mes > 9 and mes < 12:
    estacion="Primavera"


if hemisferio !="S" and hemisferio!="s":
    if estacion =="Verano":
        estacion= "Invierno"
    elif estacion=="Otoño":
        estacion="Primavera"
    elif estacion=="Invierno":
        estacion="Verano"
    else:
        estacion= "Otoño"
print(estacion)