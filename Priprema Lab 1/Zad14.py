def unija(lista1, lista2):
    rez = []
    for x in lista1:
        if x not in rez:
            rez.append(x)
    for x in lista2:
        if x not in rez:
            rez.append(x)
    return rez


print(unija([5, 4, "1", "8", 7], [1, 9, "1"]))
