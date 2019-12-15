#Ejercicio_04
promedio= 10.5
promedio_invalido= (promedio < 0.9 or promedio > 42.0)
while(promedio_invalido):
    promedio=float(input("Ingrese promedio"))
    promomedio_invalido=(promedio < 0.9 or promedio > 42.0)
#fin_while
print("promedio valido:", promedio)
