import sys

max_cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
R, C = map(int, sys.stdin.readline().split())
strings = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)]
done = [0 for _ in range(26)]
done[strings[0][0]] = 1


def dfs(x, y, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    if max_cnt == 26:
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if done[strings[nx][ny]] == 0:
                done[strings[nx][ny]] = 1
                dfs(nx, ny, cnt + 1)
                done[strings[nx][ny]] = 0


dfs(0, 0, 1)
print(max_cnt)