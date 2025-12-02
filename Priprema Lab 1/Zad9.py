def prosek(lista):
    rez = []
    for x in lista:
        if type(x).__name__ != 'list':
            raise (TypeError("Elementi liste treba da budu iskljucivo liste!"))
        sum = 0
        for y in x:
            sum += y
        rez.append(sum/len(x))
    return rez


print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))
