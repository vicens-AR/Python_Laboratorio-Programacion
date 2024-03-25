nombre = input("Hola escribe tu nombre porfavor: ")
edad = int(input("ahora tu edad porfavor: "))
ciudad = input("y por ultimo tu ciudad de residencia: ")

nacimiento = 2024 - edad

print("Hola", nombre, "de", edad, "años, nacido en el año:", nacimiento, "que vive en la ciudad llamada:", ciudad, "espero que tengas un buen dia")

if edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")

if edad % 5 == 0:
    print("Tu edad es multiplo de 5")
else:
    print("Tu edad no es multiplo de 5")