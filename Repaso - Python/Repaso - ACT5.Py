import random

Numero = int(input("Ingrese un numero entero: "))
Adivinar = random.randint(1, 100)
intentos = 0

while Numero != Adivinar:
    intentos += 1
    if Numero == Adivinar:
        print(f"Adivinaste el numero en {intentos} intentos")
        break  
    
    elif Numero > Adivinar:
        print("El numero es más pequeño.")
    else:
        print("El numero es más grande.")

#problemas con elif y else