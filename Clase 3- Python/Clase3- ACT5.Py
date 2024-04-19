def suma(num):
  return lambda a : a + num

numero = suma(2)
print(numero(11))

#suma con lambda terminado