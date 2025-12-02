def razlika(lista1, lista2):
    razl = []
    for x in lista1:
        if x not in lista2:
            razl.append(x)
    return razl


print(razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))
