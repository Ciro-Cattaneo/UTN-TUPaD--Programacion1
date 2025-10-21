alumnos = {}
suma = 0

for i in range (3):
    nombre = input ( "Ingrese el nombre del alumno  " )
    lista_notas = []

    for i in range (3):
        nota = int (input ( f"Ingrese la nota numero [{i+1}]  " ) )
        lista_notas.append(nota)
        suma += nota
    
    tupla_notas = tuple(lista_notas)
    alumnos[nombre] = tupla_notas
    
    
print(alumnos)
promedio = suma/9
print( "El promedio de las notas de los alumnos es: ",promedio )