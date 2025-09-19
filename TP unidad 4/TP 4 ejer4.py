bandera = True
suma=0
while bandera == True :
    num= int(input("Ingrese el numero a sumar "))
    if num!=0:
        suma=suma+num
    else:
        bandera = False
print("La suma de los numero es: ", suma)