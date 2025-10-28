with open ("productos.txt","r") as archivo:
    productos= []

    lineas= archivo.readlines()
    
    for i in lineas:
        linea = i.strip().split(",")
    
        prod = {}
        prod["nombre"] = linea[0]
        prod["precio"] = linea[1]
        prod["cantidad"] = linea[2]

        productos.append(prod)

print(productos)