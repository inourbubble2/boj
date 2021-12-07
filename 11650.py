N = int(input())
xys = [list(map(int, input().split())) for _ in range(N)]
xys.sort(key=lambda x:(x[0], x[1]))
for num in xys:
    print(*num)