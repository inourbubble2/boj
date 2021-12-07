DP = [0 for _ in range(301)]
stairs = [0 for _ in range(301)]

n = int(input())
for i in range(n):
    stairs[i+1] = int(input())

DP[1] = stairs[1]
DP[2] = stairs[1] + stairs[2]

for i in range(3, n+1):
    a = DP[i-2] + stairs[i]
    b = DP[i-3] + stairs[i-1] + stairs[i]
    DP[i] = max(a, b)

print(DP[n])