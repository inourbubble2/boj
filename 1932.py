N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]

DP = [[0 for _ in range(N)] for _ in range(N)]

DP[0][0] = T[0][0]

for i in range(1, N):
    for j in range(i+1):
        v = DP[i-1][j]
        if j != 0:
            v = max(v, DP[i-1][j-1])
        DP[i][j] = v + T[i][j]

print(max(DP[N-1]))