from functools import reduce


def proizvod(lista1, lista2):
    modA = [reduce(lambda x, y: x+y, podlista) for podlista in lista1]
    rez = [modA[x] * lista2[x] for x in range(0, len(lista2))]
    print(rez)


proizvod([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3])
