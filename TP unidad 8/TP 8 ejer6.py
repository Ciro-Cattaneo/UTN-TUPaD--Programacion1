with open ("productos.txt","r") as archivo:
    copia = archivo.read()

with open ("productos.txt","w") as archivo:
    archivo.write(copia)