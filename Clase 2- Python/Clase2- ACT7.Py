Cadena = "Fernando Alonso es el GOAT"
Letra_a = 0
i = 0
while len(Cadena) > i:
    if Cadena[i] == "a":
        Letra_a += 1
    elif Cadena[i] == "A":
        Letra_a += 1
    i+=1

print(f"La cantidad de letras a es: {Letra_a}")

#Terminado