N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    prevprev = 1
    prev = 2
    now = 0
    for i in range(3, N+1):
        now = (prevprev + prev) % 15746
        prevprev = prev
        prev = now

    print(now)