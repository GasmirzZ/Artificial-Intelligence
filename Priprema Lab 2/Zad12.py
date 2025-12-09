from functools import reduce


def izracunaj(lista):
    medjurez = [list(map(lambda x: x**2, item)) if type(item).__name__ == 'list' else item
                for item in lista]
    print(medjurez)
    rez = [reduce(lambda x, y: x + y, item)
           if type(item).__name__ == 'list' else item**2 for item in medjurez]
    print(rez)


izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]])
