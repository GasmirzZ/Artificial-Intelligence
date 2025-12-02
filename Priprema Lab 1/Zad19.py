def stepenuj(lista):
    rez = []
    for tup in lista:
        tmp = tup[0]
        for i in range(1, len(tup)):
            tmp = tmp ** tup[i]
        rez.append(tmp)
    return rez


print(stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]))
