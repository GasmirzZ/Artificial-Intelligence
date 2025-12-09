from itertools import zip_longest


def poredak(lista1, lista2):
    spoj = list(zip_longest(lista1, lista2, fillvalue=0))
    rez = [(el1, el2, "Jeste" if el1 * 2 <= el2 else "Nije")
           for el1, el2 in spoj]
    return rez


def poredak1(lista1, lista2):
    elNum = max(len(lista1), len(lista2))
    n1 = len(lista1)
    n2 = len(lista2)
    rez = [
        (el1, el2, "Jeste" if el1*2 <= el2 else "Nije")
        for el1, el2 in [
            (lista1[x] if x < n1 else 0, lista2[x] if x < n2 else 0) for x in range(0, elNum)
        ]
    ]
    return rez

# varijanta sa map mada ovo gore deluje lakse


def poredak2(lista1, lista2):
    elNum = max(len(lista1), len(lista2))
    n1 = len(lista1)
    n2 = len(lista2)
    rez = list(map(lambda x: (
        lambda el1, el2: (el1, el2, "Jeste" if el1 * 2 <= el2 else "Nije")
    )(
        lista1[x] if x < n1 else 0,
        lista2[x] if x < n2 else 0
    ), range(elNum)))
    return rez


print(poredak([1, 7, 2, 4], [2, 5, 2]))
print(poredak1([1, 7, 2, 4], [2, 5, 2]))
print(poredak2([1, 7, 2, 4], [2, 5, 2]))
