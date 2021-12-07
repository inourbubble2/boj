N = int(input())
A = list(map(int, input().split()))
up = [1 for _ in range(N)]
down = [1 for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            up[i] = max(up[i], up[j] + 1)
for i in range(N-1, -1, -1):
    for j in range(i-1, -1, -1):
        if A[i] < A[j]:
            down[j] = max(down[i] + 1, down[j])
for i in range(N):
    answer = max(up[i]+down[i]-1, answer)
print(answer)