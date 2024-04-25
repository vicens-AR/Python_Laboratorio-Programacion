precio = float(input("Ingrese el precio original del producto: "))
descuento = float(input("Ingrese el descuento: "))

descuentoT = descuento / 100

descuentoPesos = descuentoT * precio

precioFinal = precio - descuentoPesos

print(f"El precio final de su producto es de: {precioFinal}")

#Terminado