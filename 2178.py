from collections import deque

N, M = map(int, input().split())
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0 for _ in range(M)] for _ in range(N)]
arr = list()
for i in range(N):
    s = list(map(int, list(input())))
    arr.append(s)

queue = deque()
queue.append((0, 0))
visited[0][0] = True

while queue:
    pr, pc = queue.popleft()
    if pr == N-1 and pc == M-1:
        print(visited[pr][pc])
        break

    for r, c in direction:
        if 0 <= pr+r < N and 0 <= pc+c < M:
            if arr[pr+r][pc+c] and not visited[pr+r][pc+c]:
                visited[pr+r][pc+c] = visited[pr][pc] + 1
                queue.append((pr+r, pc+c))