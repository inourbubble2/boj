import sys
INF = 99
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
edges = dict()
distance = [INF for _ in range(V+1)]
found = [False for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if u in edges:
        edges[u].append((v, w))
    else:
        edges[u] = [(v, w)]

def choose():
    min = INF + 1
    min_pos = -1
    for i in range(1, V+1):
        if distance[i] < min and not found[i]:
            min = distance[i]
            min_pos = i
    return min_pos


def shortest_path(start):
    if start in edges:
        for v in edges[start]:
            distance[v[0]] = v[1]
    distance[start] = 0
    found[start] = True

    for i in range(1, V+1):
        if i == K:
            continue
        u = choose()
        for v in edges[u]:
            if not found[v[0]]:
                if distance[u] + v[1] < distance[v[0]]:
                    distance[v[0]] = distance[u] + v[1]


shortest_path(K)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])