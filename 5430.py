def AC(p, arr):
    error = False
    reverse_flag = False
    for c in p:
        if c == 'R':
            reverse_flag = not reverse_flag
        elif c == 'D':
            if arr:
                if reverse_flag:
                    arr.pop()
                else:
                    arr.pop(0)
            else:
                error = True
    if error:
        print('error')
    else:
        print('[', end='')
        if reverse_flag:
            for i in range(len(arr)-1, -1, -1):
                if i == 0:
                    print(arr[i], end='')
                else:
                    print(arr[i], end=',')
        else:
            for i in range(len(arr)):
                if i + 1 == len(arr):
                    print(arr[i], end='')
                else:
                    print(arr[i], end=',')
        print(']')


T = int(input())

for case in range(T):
    p = input()
    n = int(input())
    s = input().replace('[','').replace(']', '')
    if n > 0:
        arr = list(map(int, s.split(',')))
        AC(p, arr)
    else:
        AC(p, [])
