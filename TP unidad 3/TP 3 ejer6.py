#La lista será de 10 numeros que van del 1 al 10 para que el ejer sea mas visual
from statistics import mode , median,mean
import random
nums = [random.randint(1,10) for i in range(10)]
print(nums)
moda= mode(nums)
mediana= median(nums)
media= mean(nums)
print("moda", moda)
print("media",media)
print("mediana",mediana)
if media> mediana and mediana>moda:
    print("Sesgo positivo") 
elif media<mediana and mediana<moda:
    print("Sesgo negativo")
else:
    print("No hay sesgo")