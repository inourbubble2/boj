T = int(input())

for _ in range(T):
    N = int(input())
    DP = [_ for i in range(100)]
    DP[0] = 1
    DP[1] = 1
    DP[2] = 1
    DP[3] = 2
    DP[4] = 2
    # 2 + 1 = 3
    # 3 + 1 = 4
    # 4 + 1 = 5
    # 5 + 2 = 7
    # 7 + 2 = 9
    # 9 + 3 = 12
    # 12 + 4 = 16
    # 16 + 5 = 21
    # 21 + 7 = 28
    for i in range(5, N):
        DP[i] = DP[i-5] + DP[i-1]
    print(DP[N-1])
