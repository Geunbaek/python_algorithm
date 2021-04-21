# disjoint-set(union-find) Algorithm
def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    x_parent = find(x, parent)
    y_parent = find(y, parent)

    if x < y:
        parent[y_parent] = x_parent
    else:
        parent[x_parent] = y_parent

def kruskal(edges):
    edges.sort(key = lambda x:x[2])
    parent = [i for i in range(node_cnt+1)]
    mst = []
    total_weight = 0
    cnt = 0

    for edge in edges:
        start_node, end_node, weight = edge
        if find(start_node, parent) != find(end_node, parent):
            union(start_node, end_node, parent)
            mst.append(edge)
            total_weight += weight
            cnt += 1
        if cnt == node_cnt - 1:
            break
    return mst, total_weight

node_cnt, edge_cnt = map(int, input().split())
edges = []

for _ in range(edge_cnt):
    edge = list(map(int, input().strip().split()))
    edges.append(edge)

mst, total_weight = kruskal(edges)
print(mst)
print(total_weight)

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
[[3, 5, 1], [1, 2, 2], [2, 4, 3], [4, 5, 3], [3, 6, 7]]
16
"""
