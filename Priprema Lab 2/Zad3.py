from itertools import zip_longest


def spoji(lista1, lista2):
    elNum = max(len(lista1), len(lista2))
    spoj = list(zip_longest(lista1, lista2, fillvalue=0))
    rez = [(a, b, a+b) if a < b else (b, a, a+b) for a, b in spoj]
    return rez


print(spoji([1, 7, 2, 4], [2, 5, 2]))
