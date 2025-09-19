import random
rand = random.randint(1,10)
bandera = True 
cont=0
while bandera:
    num=int(input("Ingrese un numero del 1 al 10  "))
    cont+=1
    if num== rand:
        bandera=False
print(f"Felicidades acertaste en {cont} intentos")