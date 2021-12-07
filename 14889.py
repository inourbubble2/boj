from itertools import combinations

N = int(input())
player = set([i for i in range(N)])
ability = []
for i in range(N):
    ability.append(list(map(int, input().split())))
min_diff = 2147483647
comb = list(combinations([i for i in range(N)], N//2))
for start in comb[:len(comb)//2]:
    s, l = 0, 0
    link = player - set(start)
    for i in start:
        for j in start:
            if i != j:
                s += ability[i][j]
    for i in link:
        for j in link:
            if i != j:
                l += ability[i][j]
    min_diff = min(abs(s - l), min_diff)
print(min_diff)
