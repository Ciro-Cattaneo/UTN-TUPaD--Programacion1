def calcular_imc (peso,altura):
    imc = peso / (altura**2)
    return print("Su IMC es: ",imc)


peso = float(input("Ingrese su peso  "))
altura = float(input("Ingrese su altura en metros  "))

calcular_imc(peso,altura)