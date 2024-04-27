import random

Longitud = int(input("Eliga la longitud de su cadena: "))
contraseña = ""

while Longitud > len(contraseña):
    contraseña = contraseña + "2"
    if "2" in contraseña:
        contraseña = contraseña + "*"

print(f"{contraseña}")