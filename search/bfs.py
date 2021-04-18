from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now_node = q.popleft()
        print(now_node, end = " ")
        for next_node in graph[now_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

node, edges, start = map(int, input().split())
graph = [[] for _ in range(node+1)]
visited = [False] * (node+1)

for _ in range(edges):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for n in graph:
    n.sort()

bfs(start)

"""
input
4 5 1
1 2
1 3
1 4
2 4
3 4
output
1 2 3 4
"""
