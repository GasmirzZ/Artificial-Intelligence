def objedini(lista):
    rez = {t[0]: list(t[1:]) if len(t) > 2 else None for t in lista}
    print(rez)


objedini([(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)])
