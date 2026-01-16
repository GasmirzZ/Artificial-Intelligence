# Napisati funkciju koja na osnovu zadatog težinskog neusmerenog grafa i zadatog (ciljnog) čvora G
# formira neusmereni težinski graf sa heuristikom. Heuristika proizvoljnog čvora C se određuje kao
# dužina puta od čvora C do čvora G.


def nadji_heuristike(graf, cilj):
    # krecemo od cilja, svima postavimo udaljenost na beskonacno a za cilj 0
    open_set = {cilj}
    closed_set = set()
    h = {cvor: float('inf') for cvor in graf}
    h[cilj] = 0

    while open_set:
        node = min(open_set, key=lambda n: h[n])
        open_set.remove(node)
        closed_set.add(node)

        # za svakog suseda (sused, tezina grane do njega)
        for (m, cost) in graf[node]:
            if m not in closed_set:
                # udaljenost za trenutni plus cena do suseda
                nova_cena = h[node] + cost
                if nova_cena < h[m]:
                    h[m] = nova_cena
                    if m not in open_set:
                        open_set.add(m)

    # novi graf sa heuristikama
    novi_graf = {cvor: (h[cvor], graf[cvor]) for cvor in graf}
    return novi_graf


graf = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 5), ('F', 3)],
    'C': [('A', 2), ('D', 1), ('E', 3), ('G', 6)],
    'D': [('B', 5), ('C', 1), ('E', 2)],
    'E': [('C', 3), ('D', 2), ('H', 4)],
    'F': [('B', 3), ('G', 2)],
    'G': [('C', 6), ('F', 2), ('H', 1)],
    'H': [('E', 4), ('G', 1)]
}


rezultat = nadji_heuristike(graf, "H")

print("Graf sa heuristikama:")
for cvor, (h, susedi) in rezultat.items():
    print(f"{cvor}: h={h}, susedi={susedi}")
