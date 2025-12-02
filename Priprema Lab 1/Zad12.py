def presek(lista1, lista2):
    rez = []
    for x in lista1:
        if x in lista2:
            rez.append(x)
    return rez


print(presek([5, 4, "1", "8", 3, 7], [1, 9, "1"]))
