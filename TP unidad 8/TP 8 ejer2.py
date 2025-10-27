with open ("productos.txt","r") as archivo:
    a = archivo.readline().strip().split(",")
    b = archivo.readline().strip().split(",")
    c = archivo.readline().strip().split(",")
    
print(f"producto: {a[0]}|Precio: {a[1]}|Cantidad: {a[2]}")
print(f"producto: {b[0]}|Precio: {b[1]}|Cantidad: {b[2]}")
print(f"producto: {c[0]}|Precio: {c[1]}|Cantidad: {c[2]}")