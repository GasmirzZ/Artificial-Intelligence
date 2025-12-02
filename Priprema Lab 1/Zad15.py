def izdvoji(lista):
    rez = []
    n = 0
    for x in lista:
        if len(x) > n:
            rez.append(x[n])
        else:
            rez.append(0)
        n += 1
    return rez


print(izdvoji([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))
