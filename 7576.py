from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

M, N = map(int, input().split())
arr = list()
for i in range(N):
    s = list(map(int, list(input().split())))
    arr.append(s)

queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j))

while queue:
    pr, pc = queue.popleft()
    for r, c in direction:
        if 0 <= pr+r < N and 0 <= pc+c < M:
            if arr[pr+r][pc+c] == 0:
                arr[pr+r][pc+c] = arr[pr][pc] + 1
                queue.append((pr+r, pc+c))

# if 0 in sum(arr, []):
#     print(-1)
# else:
#     print(max(sum(arr, [])) - 1)

max_val = 0
is_break = False
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            max_val = 0
            is_break = True
            break
        elif arr[i][j] > max_val:
            max_val = arr[i][j]
    if is_break:
        break
print(max_val - 1)