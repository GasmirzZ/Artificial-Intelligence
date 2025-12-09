from functools import reduce


def suma(lista):
    midrez = [reduce(lambda x, y: x + y, podlista) for podlista in lista]
    rez = reduce(lambda x, y: x + y, midrez)
    print(rez)


suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
