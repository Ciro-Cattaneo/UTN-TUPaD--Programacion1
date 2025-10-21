primer_aprobado = {"Pedro","Juan","Roberto","Ciro","Agustin","Pablo"}
segundo_aprobado = {"Ciro","Andres","Horacio","Agustin","Ignacio","Gonzalo"}

print( "Los siguientes alumnos aprobaron ambos parciales: ", primer_aprobado & segundo_aprobado )

print( "Los siguientes alumnos aprobaron solo un parcial: ", primer_aprobado ^ segundo_aprobado )

print( "Los siguientes alumnos aprobaron al menos un parcial: ", primer_aprobado | segundo_aprobado )