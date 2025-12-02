def kreiraj(n):
    rez = []
    sum = 0
    for i in range(n):
        sum += (i)
        rez.append((i, sum**2))
    return rez


print(kreiraj(4))  # kod njih ovo kreira 5 elementa tkd msm da je tamo greska
