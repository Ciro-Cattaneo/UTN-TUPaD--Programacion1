productos = {"Oreo":15, "Pepitos":10 , "Toddy":0 , "Rumba":5}
bandera_menu = True

while bandera_menu :
    print("""
CONSULTAR EL STOCK DE UN PORODUCTO[1]
AGREGAR UNIDADES A UN STOCK[2]
AGREGAR UN NUEVO PRODUCTO[3]
SALIR[4]          
           """)
    menu = input("¿Que desea hacer?  ")
    
    match menu :
        
        case "1":
            producto_buscar = input("Ingrese el producto a buscar  ")
            producto_buscar = producto_buscar.capitalize()
            
            if producto_buscar in productos:
                print(f"EL producto {producto_buscar} tiene {productos[producto_buscar]} en stock")
            else:
                print("No se encontró el producto")
            
        case "2":
            producto_buscar = input("Ingrese el producto a buscar ")
            producto_buscar = producto_buscar.capitalize()

            if producto_buscar in productos:
               stock = int( input ( "Ingrese la cantidad de stock del producto  " ))
               productos[producto_buscar] = stock
            else:
                print("No se encontró el producto")
        case "3":
            nuevo = input ( "Ingrese un nuevo producto  " )
            nuevo = nuevo.capitalize()

            if nuevo in productos:
                print( "El producto ya es parte del catalogo" )
            
            else:
                productos[nuevo] = int( input( "Ingrese la cantidad en stock" ) )

        case "4":
            bandera_menu = False


