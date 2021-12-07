DP = [0 for _ in range(21)]
DP[0] = 0
DP[1] = 1

n = int(input())

for i in range (2, n + 1):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[n])