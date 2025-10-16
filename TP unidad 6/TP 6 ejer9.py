def celsius_a_farenheit (celsius):
    return (celsius * (9/5)) +32

grados = float(input("Ingrese la temperatura en Celsius  "))
print(f"La temperatura en Farenheit es  {celsius_a_farenheit(grados)}")