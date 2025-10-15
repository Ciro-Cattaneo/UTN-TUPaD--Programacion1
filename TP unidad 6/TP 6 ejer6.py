def tabla_multiplicar (numero):
    for i in range (1,11):
        print (f"{numero} x {i} = {numero*i}")
    

num = int ( input("Ingrese el numero a multiplicar  ") )

tabla_multiplicar(num)