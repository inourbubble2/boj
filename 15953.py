rank_17 = [1, 2, 3, 4, 5, 6]
prize_17 = [500, 300, 200, 50, 30, 10]
for i in range(1, len(rank_17)):
    rank_17[i] = rank_17[i - 1] + rank_17[i]

rank_18 = [1, 2, 4, 8, 16]
prize_18 = [512, 256, 128, 64, 32]
for i in range(1, len(rank_18)):
    rank_18[i] = rank_18[i - 1] + rank_18[i]

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    prize = 0
    if a != 0:
        for i in range(len(rank_17)):
            if rank_17[i] >= a:
                prize += prize_17[i]
                break
    if b != 0:
        for i in range(len(rank_18)):
            if rank_18[i] >= b:
                prize += prize_18[i]
                break
    print(prize*10000)
