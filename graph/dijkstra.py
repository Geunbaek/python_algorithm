import heapq

def dijkstra(start):
    distance[start] = 0
    for next_node, val in graph[start]:
        heapq.heappush(q, (val, next_node))
    while q:
        current_distance, current_node = heapq.heappop(q)
        if distance[current_node] > current_distance:
            distance[current_node] = current_distance
            for next_node, val in graph[current_node]:
                heapq.heappush(q, (current_distance + val, next_node))

node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]
distance = [float('inf') for _ in range(node+1)]
q = []

for _ in range(edge):
    start, end, value = map(int, input().strip().split())
    graph[start].append((end, value))

dijkstra(1)
print(distance[1:])

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
[0, 2, 4, 5, 5, 11]
"""