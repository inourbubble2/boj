N, L = map(int, input().split())
roads = []
for _ in range(N):
    roads.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N - L - 1):
        is_same = True
        for k in range(j, j + L - 1):
            if roads[i][k] != roads[i][k + 1]:
                is_same = False
        for k in range(j + L, j + L + L - 1):
            if roads[i][k] != roads[i][k + 1]:
                is_same = False
        if is_same:
            diff = roads[i][j] - roads[i][j+L]
            if diff == -1:
                roads[i][j] += 0.5
                roads[i][j+1] += 0.5
            elif diff == 1:
                roads[i][j + 2] += 0.5
                roads[i][j + 3] += 0.5
for road in roads:
    print(*road)

