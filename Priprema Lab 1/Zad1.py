def parni(lista):
    parni = []
    neparni = []
    for i in lista:
        if type(i) not in (int, float):
            continue
        elif i % 2 == 0:
            parni.append(i)
        else:
            neparni.append(i)
    return {'Parni': parni, 'Neparni': neparni}


print(parni([1, "2", 3, 4, 5]))
