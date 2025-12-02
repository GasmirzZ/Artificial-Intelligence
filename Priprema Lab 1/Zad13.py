def izmeni(lista):
    pp = []
    np = []
    for x in range(len(lista)):
        if x % 2 == 1:
            np.append(lista[x]-1)
        else:
            pp.append(lista[x]+1)
    return {"pp": pp, "np": np}


print(izmeni([8, 6, 3, 1, 1]))
