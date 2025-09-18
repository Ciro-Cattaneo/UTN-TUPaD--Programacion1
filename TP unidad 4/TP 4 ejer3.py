print("vamos a sumar todos los números enteros comprendidos entre dos valores")
num1=int(input("Ingrese el primer valor "))
num2=int(input("Ingrese el segundo valor "))
suma=0
for i in range(num1+1,num2):
    suma=suma+i
print("La suma es ",suma)