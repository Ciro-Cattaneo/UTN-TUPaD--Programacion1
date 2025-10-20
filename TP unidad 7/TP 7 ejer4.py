contactos = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto numero {i+1}  ")
    contactos[nombre] = int(input("Ingrese su numero de telefono  "))

nombre_buscar = input("Ingrese el nombre a buscar  ")
if nombre_buscar in contactos:
    print(f"El contacto de {nombre_buscar} es: {contactos[nombre_buscar]}")    
