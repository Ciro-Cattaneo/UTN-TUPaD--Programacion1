suma=0
cant=10
print("Ingrese ",cant," numeros para sacar su media")
for i in range(cant):
    num=int(input(f"Ingrese el numero {i+1} "))
    suma=suma+num
print(f"La media de los numeros ingresados es: {suma/cant}")