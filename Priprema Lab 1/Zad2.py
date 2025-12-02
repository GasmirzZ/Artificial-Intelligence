def numlista(lista):
    dict = {}
    for x in lista:
        tip = type(x).__name__
        dict.setdefault(tip, []).append(x)
    return dict


print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]]))
