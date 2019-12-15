#Ejercicio_02
talla= 1.50
talla_invalida= (talla < 1.60 or talla > 1.90)
while(talla_invalida):
    talla=float(input("Ingrese talla"))
    talla_invalida=(talla < 1.60 or talla > 1.90)
#fin_while
print("talla valida:", talla)
