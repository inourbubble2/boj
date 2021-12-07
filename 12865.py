N, K = map(int, input().split())
W = [0 for _ in range(N+1)]
V = [0 for _ in range(N+1)]
DP = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    w, v = map(int, input().split())
    W[i], V[i] = w, v
for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= W[i]:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-W[i]]+V[i])
        else:
            DP[i][j] = DP[i-1][j]
print(DP)
print(DP[N][K])