import math


T = int(input())
for _ in range(T):
    coord = []
    for __ in range(4):
        x, y = map(int, input().split())
        coord.append((x, y))
    coord.sort(key=lambda a: (a[0], a[1]))

    x1 = (coord[0][0] - coord[3][0]) ** 2
    y1 = (coord[0][1] - coord[3][1]) ** 2
    l1 = math.sqrt(x1 + y1)
    x2 = (coord[1][0] - coord[2][0]) ** 2
    y2 = (coord[1][1] - coord[2][1]) ** 2
    l2 = math.sqrt(x2 + y2)
    if l1 == l2:
        print(1)
    else:
        print(0)