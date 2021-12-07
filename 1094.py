X = int(input())
if X == 64:
    print(1)
else:
    curr = 64
    sticks = 0
    cnt = 0
    while sticks != X:
        divided = curr // 2
        if sticks + divided <= X:
            sticks += divided
            cnt += 1
        curr = divided
    print(cnt)