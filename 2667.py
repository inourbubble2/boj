N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x, y, c):
    if arr[x][y] == '1':
        arr[x][y] = c
        visited[x][y] = True
        for xx, yy in direction:
            if 0 <= x+xx < N and 0 <= y+yy < N:
                if arr[x+xx][y+yy] == '1' and not visited[x+xx][y+yy]:
                    dfs(x+xx, y+yy, c)


cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            cnt += 1
            dfs(i, j, str(cnt))

arr = sum(arr, [])
print(cnt)
result = []
for i in range(1, cnt+1):
    result.append(arr.count(str(i)))

result.sort()
for i in range(cnt):
    print(result[i])