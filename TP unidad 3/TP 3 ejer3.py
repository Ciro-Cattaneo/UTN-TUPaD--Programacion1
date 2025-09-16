bandera=True
while bandera:
    numero=int(input("Ingrese un numero par  "))
    if numero%2 == 0:
        print("Ha ingresado un numero par")
        bandera = False
    else:
        print("Por favor, ingrese un número par")
print("chau")