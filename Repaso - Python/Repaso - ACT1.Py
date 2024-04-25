altura = float(input("ingrese su altura en metros: "))
peso = float(input("ingrese su peso en kg: "))
talla = ""

IMC = peso / (altura * altura)


if IMC < 18.5:
    talla = "talla S"
elif IMC < 24.9:
    talla = "talla M"
elif IMC < 29.9:
    talla = "talla X"
else:
    talla = "talla XL"
    
print(f"su IMC es igual a: {IMC} por lo que usted es de talla: {talla}")