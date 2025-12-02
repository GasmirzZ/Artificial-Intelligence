def izbroj(lista):
    sum = 0
    for x in lista:
        if type(x).__name__ == 'list':
            sum += izbroj(x)
        else:
            sum += 1
    return sum


print(izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))
