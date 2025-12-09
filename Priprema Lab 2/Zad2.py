from itertools import zip_longest


def spojidict(lista1, lista2):
    elNum = max(len(lista1), len(lista2))
    spoj = list(zip_longest(lista1, lista2, fillvalue='-'))
    rez = [{'prvi': a, 'drugi': b} for a, b in spoj]
    return rez


print(spojidict([1, 7, 2, 4], [2, 5, 2]))
