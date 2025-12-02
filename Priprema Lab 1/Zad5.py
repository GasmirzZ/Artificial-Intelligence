def brojel(lista):
    num = []
    for x in lista:
        if type(x).__name__ == 'list':
            num.append(len(x))
        else:
            num.append(-1)
    return num


print(brojel([[1, 2, 3], [1], 2, "str", [], [2, 3, 4, 5, 6]]))
