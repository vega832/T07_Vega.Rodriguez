#EJERCICIO 1
edad=30
edad_invalido=(edad<90 and edad >100)
while(edad_invalido):
    edad=int(input("tu edad es:"))
    edad_invalido=(edad<90) and (edad >100)
#fin_while
print("edad valida:",edad)
