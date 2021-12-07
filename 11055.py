N = int(input())
A = list(map(int, input().split()))
DP = [0 for _ in range(N)]

for i in range(N):
    DP[i] = A[i]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + A[i])

print(max(DP))