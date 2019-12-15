#EJERCICIO 3
resultado =""
resultado_invalido=(resultado!="tranquila" or resultado!="intranquila")
while(resultado_invalido):
    resultado=input("ingrese resultado(tranquila o intraquila ):")
    resultado_invalido=(resultado!="tranquila" or resultado!="intranquila")
#fin_while
print("resultado:",resultado)
