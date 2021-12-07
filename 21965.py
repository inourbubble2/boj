N = int(input())
arr = list(map(int, input().split()))

result = True
top = False
for i in range(1, N):
    if not top:
        if arr[i] > arr[i-1]:
            pass
        elif arr[i] < arr[i-1]:
            top = True
        else:
            result = False
    else:
        if arr[i] < arr[i - 1]:
            pass
        elif arr[i] > arr[i - 1]:
            result = False
        else:
            result = False

if result:
    print('YES')
else:
    print('NO')