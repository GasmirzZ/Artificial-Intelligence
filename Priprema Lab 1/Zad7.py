def saberi(lista):
    rez = []
    for x in lista:
        zbir = 0
        for y in x:
            zbir += y
        rez.append(zbir)
    return rez


print(saberi([(1, 4, 6), (2, 4), (4, 1)]))
