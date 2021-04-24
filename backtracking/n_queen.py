def is_avalible(graph, x, y):

    for i in range(y-1, -1, -1):
        if graph[i][x] == 1:
            return False
    for i, j in zip(range(y-1, -1, -1), range(x-1, -1, -1)):
        if graph[i][j] == 1:
            return False
    for i, j in zip(range(y-1, -1, -1), range(x+1, n)):
        if graph[i][j] == 1:
            return False
    return True

def solve_n_queen(n, graph, y):
    if n == y:
        for line in graph:
            print(line)
        print()
        return

    for x in range(n):
        if is_avalible(graph, x, y):
            graph[y][x] = 1
            solve_n_queen(n, graph, y+1)
            graph[y][x] = 0

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
solve_n_queen(n, graph, 0)

"""
input 
4
output
[0, 1, 0, 0]
[0, 0, 0, 1]
[1, 0, 0, 0]
[0, 0, 1, 0]

[0, 0, 1, 0]
[1, 0, 0, 0]
[0, 0, 0, 1]
[0, 1, 0, 0]
"""