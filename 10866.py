from sys import stdin
from collections import deque
queue = deque()
N = int(input())

for i in range(N):
    s = stdin.readline().split()
    if s[0] == 'push_front':
        queue.appendleft(s[1])
    elif s[0] == 'push_back':
        queue.append(s[1])
    elif s[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif s[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(queue))
    elif s[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)
