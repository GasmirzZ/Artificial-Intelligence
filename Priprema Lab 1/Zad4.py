def zbir(lista):
    zbir = []
    for x in range(len(lista)-1):
        zbir.append(lista[x] + lista[x+1])
    return zbir


print(zbir([2, 5, 1, 7, 0, 2]))
