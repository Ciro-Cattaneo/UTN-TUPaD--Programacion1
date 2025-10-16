def operaciones_basicas (a, b):
    ola =(["suma = ",a+b] , ["resta = ",a-b] , ["multiplicacion = ", a*b] , ["division = ",a/b])
    return print("El resultado de las operaciones con los numeros es: ",ola)


num1 = int(input("Ingrese el primer numero " ))
num2 = int(input("Ingrese el segundo numero "))

operaciones_basicas(num1,num2)