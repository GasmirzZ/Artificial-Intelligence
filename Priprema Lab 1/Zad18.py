def kreiraj(lista):
    rez = []
    for index in range(len(lista)-1):
        tmp = []
        for item in lista[index]:
            if item not in lista[index+1]:
                tmp.append(item)
        rez.append(tmp)
    return rez


print(kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]))
