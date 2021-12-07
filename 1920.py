A = dict()
N = int(input())
for num in list(map(int, input().split())):
    A[num] = True
M = int(input())
for num in list(map(int, input().split())):
    if num in A:
        print(1, end=' ')
    else:
        print(0, end=' ')

