from functools import reduce


def zamena(lista, x):

    rez = [lista[i] if lista[i] >= x else sum(
        lista[i+1:]) for i in range(0, len(lista))]
    print(rez)


zamena([1, 7, 5, 4, 9, 1, 2, 7], 5)
