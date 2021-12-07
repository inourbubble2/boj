N = int(input())
T = [0 for _ in range(N)]
P = [0 for _ in range(N)]
DP = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p
print(T, P)
for i in range(N):
    left = 0
    for j in range(N):
        if left > 0:
            left -= 1
        elif i == j and j + T[j] <= N:
            DP[i][j] = P[j]
            left = T[j] - 1
        elif (i >= j + T[j] or j > i) and j + T[j] < N:
            DP[i][j] = P[j]
            left = T[j] - 1

max_value = 0
for i in range(N):
    max_value = max(sum(DP[i]), max_value)
print(max_value)
