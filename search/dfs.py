import sys

input = sys.stdin.readline

def dfs(start):
    print(start, end = " ")
    visit[start] = 1
    for i in graph[start]:
        if not visit[i]:
            dfs(i)

node, edges, start = map(int, input().split())
graph = [[] for _ in range(node+1)]
visit = [0 for _ in range(node+1)]

for _ in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)


"""
input
4 5 1
1 2
1 3
1 4
2 4
3 4
output
1 2 4 3
"""






