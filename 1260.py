from collections import deque

N, M, V = map(int, input().split())
nodes = [[False for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for m in range(M):
    A, B = map(int, input().split())
    nodes[A][B] = True
    nodes[B][A] = True


def dfs(node):
    print(node, end=' ')
    visited[node] = True
    for i in range(1, N+1):
        if nodes[node][i] and not visited[i]:
            dfs(i)


def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    while queue:
        popped = queue.popleft()
        print(popped, end=' ')
        for i in range(1, N+1):
            if nodes[popped][i] and not visited[i]:
                visited[i] = True
                queue.append(i)


dfs(V)
print()
visited = [False for _ in range(N+1)]
bfs(V)