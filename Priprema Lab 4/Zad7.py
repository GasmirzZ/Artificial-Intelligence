from itertools import permutations

grid = [[1, 0, 0], [0, 0, 0], [0, 0, 3]]
fixed = {0: 1, 8: 3}
empty = [i for i in range(9) if i not in fixed]
for p in permutations([n for n in range(1, 10) if n not in fixed.values()]):
    for k, i in enumerate(empty):
        grid[i//3][i % 3] = p[k]
    if all(sum(row) == 15 for row in grid) and all(sum(grid[i][j] for i in range(3)) == 15 for j in range(3)):
        for row in grid:
            print(row)
        break
