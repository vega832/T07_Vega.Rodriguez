#Ejercicio_01
sueldo_quincenal= 1800
sueldo_invalido= (sueldo_quincenal < 1850 or sueldo_quincenal > 2800)
while(sueldo_invalido):
    sueldo_quincenal=float(input("Ingrese sueldo"))
    sueldo_invalido=(sueldo_quincenal < 1850 or sueldo_quincenal > 2800)
#fin_while
print("sueldo valido:", sueldo_quincenal)
