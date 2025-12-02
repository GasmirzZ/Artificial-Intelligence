def razlika(lista):
    rez = []
    for x in range(len(lista)-1):
        rez.append(lista[x] - lista[x+1])
    return rez


print(razlika([8, 5, 3, 1, 1]))
