notas=[]
suma=0
for i in range(10):
    nota=int(input(f"Ingrese la nota del alumno numero {i+1}  "))
    notas.append(nota)
    suma+=nota
print(notas)
print("El promedio de notas es:  ",suma/10) 
baja=min(notas)
alta=max(notas)
print(f"La nota mas baja es {baja} y la mas alta es {alta}")