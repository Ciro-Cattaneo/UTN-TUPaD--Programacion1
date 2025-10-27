original = {"Argentina":"Buenos Aires", "Chile":"Santiago" , "Uruguay":"Montevideo"}
lista_paises = list(original.keys())
lista_capitales = list(original.values())
invertido = {}
for i in range (len(lista_paises)):
    invertido[lista_capitales[i]] = lista_paises[i]
print(original)
print(invertido)