oracion = input( "Ingrese una oracion  " )
recuento = {}
for i in oracion :
    recuento[i] = {i.count(oracion)}


plabras_unicas = set(recuento   )


print(recuento)
print(plabras_unicas)