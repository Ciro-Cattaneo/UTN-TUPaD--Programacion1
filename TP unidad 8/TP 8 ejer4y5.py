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


nombre = input("Ingrese el nombre del producto a buscar  ")
bandera = True
for i in productos:
    
    if nombre == i["nombre"]:
        bandera = False
        print ("Los datos del producto son: ",i)

if bandera == True:
    print("No se encontró el producto")
