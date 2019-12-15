#Ejercicio_05
peso= 65
peso_invalido= (peso < 75 or peso > 90)
while(peso_invalido):
    peso=float(input("Ingrese peso"))
    peso_invalido=(peso < 75 or peso > 90)
#fin_while
print("peso valido:", peso)
