def brojanje(recnik):
    if type(recnik).__name__ != 'dict':
        raise (TypeError("Unesite recnik kao parametar"))
    rec = {}
    rez = []
    for x in recnik.values():
        tip = type(x).__name__
        rec[tip] = rec.get(tip, 0) + 1
    for x in rec.keys():
        rez.append((x, rec[x]))
    return rez


print(brojanje({1: 4, 2: [2, 3], 3: [5, 6], 4: 'test', 5: 9, 6: 8}))
