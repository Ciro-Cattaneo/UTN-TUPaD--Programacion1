print("Cargue 5 productos en la lista ")
lista=[]
for i in range (5):
    prod=input("Introduzca el producto  ")
    lista.append(prod)
lista_orden= sorted(lista)
print(lista_orden)
elim= input("Elimine un producto  ")
lista_orden.remove(elim)
print(lista_orden)