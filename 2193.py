N = int(input())
DP = [0 for _ in range(91)]

DP[1] = 1
DP[2] = 1
DP[3] = 2
for i in range(4, N+1):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[N])