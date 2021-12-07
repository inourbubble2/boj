DP = [0 for _ in range(12)]
DP[1] = 1
DP[2] = 2
DP[3] = 4

for j in range(4, 11):
    DP[j] = DP[j-1] + DP[j-2] + DP[j-3]

T = int(input())
for t in range(T):
    n = int(input())
    print(DP[n])