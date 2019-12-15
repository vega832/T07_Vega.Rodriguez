#EJERCICIO 2
resultado =""
resultado_invalido=(resultado!="bien" and resultado!="mal")
while(resultado_invalido):
    resultado=input("ingrese resultado(bien o mal):")
    resultado_invalido=(resultado!="bien" and resultado!="mal")
#fin_while
print("resultado:",resultado)
