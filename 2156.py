N = int(input())
DP = [0 for _ in range(10000)]
G = [0 for _ in range(10000)]
for i in range(N):
    G[i] = int(input())

DP[0] = G[0]

DP[1] = G[0] + G[1]
DP[2] = max(G[0] + G[1], G[1] + G[2], G[0] + G[2])

for i in range(3, N):
    a = G[i] + DP[i-2]
    b = G[i] + G[i-1] + DP[i-3]
    c = DP[i-1]
    DP[i] = max(a, b, c)

print(max(DP))