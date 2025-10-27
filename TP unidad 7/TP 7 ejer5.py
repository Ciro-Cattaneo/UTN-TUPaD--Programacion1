oracion = input( "Ingrese una oracion  " )
lista_oracion = (oracion.split())
recuento = {}


for i in lista_oracion:
    recuento [i] = lista_oracion.count(i)


palabras_unicas = set(lista_oracion)

print(palabras_unicas)
print(recuento)