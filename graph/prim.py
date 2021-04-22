import heapq
from collections import defaultdict

def prim(start, graph):
    q = graph[start]
    heapq.heapify(q)
    visited = [start]
    total_weight = 0
    mst = []
    while q:
        weight, start_node, end_node = heapq.heappop(q)
        if end_node not in visited:
            visited.append(end_node)
            mst.append([weight, start_node, end_node])
            total_weight += weight
            for edge in graph[end_node]:
                if edge[2] not in visited:
                    heapq.heappush(q, edge)
    return mst, total_weight


node_cnt, edge_cnt = map(int, input().split())
graph = defaultdict(list)

for _ in range(edge_cnt):
    start_node, end_node, weight = map(int, input().split())
    graph[start_node].append([weight, start_node, end_node])
    graph[end_node].append([weight, end_node, start_node])

print(prim(1, graph))



"""
input 
6 6
1 2 2
1 3 4
2 4 3
3 5 1
3 6 7
4 5 3
output 
([[2, 1, 2], [3, 2, 4], [3, 4, 5], [1, 5, 3], [7, 3, 6]], 16)
"""