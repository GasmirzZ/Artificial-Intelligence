def stepen(lista):
    rez = [lista[i] ** lista[i+1] for i in range(0, len(lista)-1)]
    print(rez)


stepen([1, 5, 2, 6, 1, 6, 3, 2, 9])
