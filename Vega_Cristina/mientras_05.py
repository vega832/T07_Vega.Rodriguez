#EJERCICIO 5
usuario="cristina"
telefono=7789
respuesta_invalida=(usuario!=usuario and usuario!=telefono)
while(respuesta_invalida):
    usuario=input("ingrese usuario")
    telefono=input("ingrese telefono")
    respuesta_invalida=(usuario!=usuario and usuario!=telefono)
#Fin_while
print("valido:",usuario,telefono)
