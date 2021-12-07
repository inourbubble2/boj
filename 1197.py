import sys
import heapq

V, E = map(int, input().split())
parents = [i for i in range(V+1)]
edges = []
MST = []


def find(idx):
    if parents[idx] != idx:
        return find(parents[idx])
    return idx


def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for i in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (C, A, B))

count = 0
weight = 0
while count != V - 1:
    C, A, B = heapq.heappop(edges)
    if find(A) == find(B):
        pass
    else:
        union(A, B)
        weight += C
        count += 1

print(weight)