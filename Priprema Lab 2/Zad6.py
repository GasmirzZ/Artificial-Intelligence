from itertools import zip_longest


def objedini(lista1, lista2):
    elNum = max(len(lista1), len(lista2))
    spoj = list(zip_longest(lista1, lista2, fillvalue=0))
    rez = [(a, b) if a < b else (b, a) for a, b in spoj]
    print(rez)


objedini([1, 7, 2, 4, 5], [2, 5, 2])
