edad=int(input("Ingrese su edad  "))
if edad<12 and edad>=0 :
    print("Niño/a")
elif edad>= 12 and edad<18:
    print("Adolescente")
elif edad>= 18 and edad<30:
    print("Adulto joven")
elif edad>= 30 and edad<200:
    print("Adulto")
elif edad>=200:
    print("Bienvenida señora Legrand")
else:
    print("Ingrese una edad valida")