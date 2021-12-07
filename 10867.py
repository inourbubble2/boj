N = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[0], end=' ')

for i in range(1, N):
    if arr[i-1] != arr[i]:
        print(arr[i], end=' ')