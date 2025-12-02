def uredi(lista, N, dx):
    for x in range(len(lista)):
        if x < N:
            lista[x] = lista[x] + dx
        else:
            lista[x] = lista[x] - dx
    return lista


print(uredi([2, 3, 4, 5, 6, 7, 8], 3, 1))
