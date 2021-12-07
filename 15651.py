N, M = map(int, input().split())
items = [i for i in range(1, N+1)]
visited = []


def solution():
    if len(visited) == M:
        print(*visited)
    else:
        for item in items:
            visited.append(item)
            solution()
            visited.pop()


solution()