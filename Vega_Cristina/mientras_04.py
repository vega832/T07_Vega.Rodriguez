#EJERCICIO 4
edad=0
edad_invalido=(edad<0 and edad >120)
while(edad_invalido):
    edad=int(input("ingrese edad es:"))
    edad_invalido=(edad<0) and (edad >120)
#fin_while
print("edad valida:",edad)
