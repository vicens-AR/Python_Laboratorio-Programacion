numero = int(input("ingrese unnum para la secuencia de fibbonaci: "))
i = 0
foobonaci = [0,1]

while i < numero:
    suma = foobonaci[i] + foobonaci[i+1]
    foobonaci.append(suma)
    i+=1

print(foobonaci)