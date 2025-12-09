from functools import reduce


def izracunaj(lista):
    rez = [
        reduce(lambda x, y: x*y, item)
        if type(item).__name__ == 'list'
        else item for item in lista]
    print(rez)


izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]])
