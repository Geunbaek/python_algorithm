from collections import deque

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
q = deque()
result = []

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

for i in result:
    print(i, end = " ")


'''
[Input Example 1]
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
[Output Example 1]
1 2 5 3 6 4 7
'''