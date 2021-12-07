n = int(input())
color = [[] for _ in range(n+1)]
for i in range(1, n+1):
    color[i] = list(map(int, input().split(' ')))

DP = [[0 for _ in range(3)] for _ in range(n+1)]
for i in range(1, n+1):
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + color[i][0]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + color[i][1]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + color[i][2]

print(min(DP[n]))