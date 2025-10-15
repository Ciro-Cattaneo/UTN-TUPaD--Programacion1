def segundos_a_horas (segundos):
    return segundos/60/60 

segundos = int(input("Ingrese la cantidad de segundos  "))


print(f"La cantidad de horas que representan los {segundos} segundos ingresados son {segundos_a_horas(segundos)}")