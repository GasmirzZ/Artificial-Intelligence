from itertools import zip_longest


def skupi(lista):
    rez = [[a + b for a, b in zip_longest(lista[i], lista[i+1], fillvalue=0)]
           for i in range(0, len(lista)-1)]

    print(rez)


skupi([[1, 3, 5], [2, 4, 6], [1, 2]])
