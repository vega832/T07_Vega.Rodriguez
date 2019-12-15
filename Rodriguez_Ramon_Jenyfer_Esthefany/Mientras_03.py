#Ejercicio_03
edad=25
edad_invalida=(edad < 27 or edad > 95)
while(edad_invalida):
    edad=int(input("Ingrese edad"))
    edad_invalida=(edad < 27 or edad > 95)
#fin_while
print("edad valida:", edad)
