nombre= input("Ingrese su nombre  ")
print("[1] Mayusculas")
print("[2] Minusculas")
print("[3] Primera letra mayuscula")
opc= input("Ingrse la opcion deseada  ")
if opc =="1":
    print(str.upper(nombre))
elif opc=="2":
    print(str.lower(nombre))
elif opc =="3":
    print(str.title(nombre))
else:
    print("Ingrese una opcion valida")