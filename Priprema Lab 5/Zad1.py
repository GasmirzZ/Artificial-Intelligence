COLORS = ['R', 'G', 'B']


def select_mrv_variable(domains, assignment):
    # lista neobojenih cvorova
    unassigned = [v for v in domains if v not in assignment]
    # onaj koji ima najmanje mogucnosti, tj. najmanji domen
    return min(unassigned, key=lambda v: len(domains[v]))


def is_consistent(var, color, assignment, graph):
    # prolazimo kroz sve susede cvora var i gledamo da slucajno neko oko njega nema boju koju hocemu da mu stavimo
    for n in graph[var]:
        if assignment.get(n) == color:
            return False  # ima suseda sa istom bojom
    return True  # nema konflikta


def forward_checking(var, color, domains, graph):
    for n in graph[var]:
        if color in domains[n]:
            domains[n].remove(color)  # uklanja boju iz domena

            if not domains[n]:
                return False  # domen suseda prazan i to je greska idemo nazad
    return True


def backtracking(assignment, domains, graph):
    if len(assignment) == len(domains):
        return assignment

    var = select_mrv_variable(domains, assignment)

    # prolazzi se kroz kopiju domena da bi se izbegle modifikacije tokom iteracije
    for color in list(domains[var]):
        if is_consistent(var, color, assignment, graph):
            assignment[var] = color

            # kopija domena pre Forward Checking, lakse vracanje starih vrednosti
            old_domains = {v: list(d) for v, d in domains.items()}
            domains[var] = [color]  # domen dobija izabranu boju

            success = forward_checking(var, color, domains, graph)
            if success:
                result = backtracking(assignment, domains, graph)
                if result:
                    return result

            # Ako nismo uspeli, vracamo stare domene (backtrack) i pokusavamo drugu boju
            domains = old_domains
            del assignment[var]

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

graph_2 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}


domains = {v: COLORS.copy() for v in graph_2}  # 'A': {'R', 'G', 'B'}, ...
solution = backtracking({}, domains, graph_2)
print(solution)
