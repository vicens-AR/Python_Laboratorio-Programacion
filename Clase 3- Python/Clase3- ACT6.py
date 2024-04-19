def sumas(numeros):
    cuadrados = map(lambda x: x**2 , numeros)
    return list(cuadrados)

print(sumas([1,2,3,4]))

#hago con un map una potencia de cada numero de la lista de numeros