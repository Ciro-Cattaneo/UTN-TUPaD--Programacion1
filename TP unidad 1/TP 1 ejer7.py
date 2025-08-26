num1=int(input("Ingrese el primer numero(debe ser distinto a 0) "))
num2=int(input("Ingrese el segundo numero(debe ser distinto a 0) "))
if num1!=0 and num2 !=0 :
    print(f"{num1} + {num2}= {num1+ num2}")
    print(f"{num1} - {num2}= {num1- num2}")
    print(f"{num1} * {num2}= {num1* num2}")
    print(f"{num1} / {num2}= {num1/ num2}")
else :
    print("numero no valido")
    