contraseña = input("cree una contraseña: ")
j = 0
numeros = ["0","1","2","3","4","5","6","7","8","9"]
i = 0

if len(contraseña) < 8:
    print("Su contraseña no es valida")

while len(numeros) > j:
    if contraseña[j] != numeros[i]:
        i +=1
    else:
        print("tiene numero")
    j+=1

print("su contraseña es valida")


#sin terminar