DP = [(0, 0) for _ in range(41)]
DP[0] = (1, 0)
DP[1] = (0, 1)
DP[2] = (1, 1)

for i in range(3, 41):
    DP[i] = (DP[i-1][1], DP[i-1][0] + DP[i-1][1])

T = int(input())
for t in range(T):
    N = int(input())
    print(DP[N][0], DP[N][1])