from functools import reduce


def proizvod(lista):
    medjurez = [reduce(lambda x, y: x*y, podlista) for podlista in lista]
    rez = reduce(lambda x, y: x*y, medjurez)
    print(rez)


proizvod([[1, 3, 5], [2, 4, 6], [1, 2, 3]])
