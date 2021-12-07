import sys
sys.setrecursionlimit(10000)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x, y, c):
    if arr[x][y]:
        arr[x][y] = c
        visited[x][y] = True
        for xx, yy in direction:
            if 0 <= x+xx < N and 0 <= y+yy < M:
                if arr[x+xx][y+yy] and not visited[x+xx][y+yy]:
                    dfs(x+xx, y+yy, c)


T = int(input())
for testcase in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for cabbage in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                cnt += 1
                dfs(i, j, cnt)
    print(cnt)
