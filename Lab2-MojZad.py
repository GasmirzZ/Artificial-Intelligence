from functools import reduce


def suma(lista):
    rez = reduce(lambda x, y: x+y,
                 [reduce(lambda x, y: x+y, sublist) for sublist in lista])
    print(rez)


suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
