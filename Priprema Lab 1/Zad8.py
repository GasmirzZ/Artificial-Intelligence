def izmeni(lista):
    for x in range(1, len(lista)):
        lista[x] += lista[x-1]
    return lista


print(izmeni([1, 2, 4, 7, 9]))
