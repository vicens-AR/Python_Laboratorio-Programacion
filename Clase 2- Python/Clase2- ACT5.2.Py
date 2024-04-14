frutas = ["manzana", "pera", "banana", "frutilla", "uva"]
fruta = input("escribe una fruta sin mayusculas: ")
i = 0

while len(frutas) > i:
    if frutas[i] != fruta:
        i += 1
    else:
        print(f"su fruta {fruta} se encuentra en la lista")
        i+=1
    


#falta alerta para cuando no esta tu fruta pero no se como hacerla
