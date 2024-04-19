def palindromo(palabra):
    ultimo = len(palabra) - 1
    i = 0
    while i <  len(palabra) / 2:
        if palabra[i] == palabra[ultimo]:
            i += 1
            ultimo -=1
        else:
            return False
    return True

print(palindromo("oro"))

#terminado