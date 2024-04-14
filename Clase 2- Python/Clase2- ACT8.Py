lista = []
nombre=""
empieza_a = 0
empieza_e = 0
i = 0

while nombre != "fin":
    nombre = input("escribi un nombre: ")
    lista.append(nombre)
    if nombre[0] == "a":
        empieza_a +=1
    elif nombre[0] == "A":
        empieza_a +=1
    elif nombre[0] == "e":
        empieza_e +=1
    elif nombre[0] == "E":
        empieza_e +=1

#este if se lo pedi a chat gpt, porque no sabia como sacar el fin
if "fin" in lista:
    lista.remove("fin")


lista.sort()

print(f"los nombres que ingresaste son: {lista}")
print(f"los nombre que empiezan con a son: {empieza_a}")
print(f"los nombre que empiezan con e son: {empieza_e}")

#terminado aaaaaaaaaaaaaaa