cont0=0
par=0
impar=0
pos=0
neg=0
for i in range(100):
    num= int(input("Ingrese un numero  "))
    if num==0:
        cont0+=1
    elif num%2==0:
        par+=1
    else:
        impar+=1
    if num>0:
        pos+=1
    elif num<0:
        neg+=1
print("////////////////////////")
print("numeros pares",par)
print("numeros impares",impar)
print("numeros positivos",pos)
print("numeros negativos",neg)
print("numeros ceros",cont0)