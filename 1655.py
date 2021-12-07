import heapq
import sys


N = int(sys.stdin.readline())
min_heap, max_heap = [], []

for _ in range(N):
    num = int(sys.stdin.readline())

    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))

    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-min_value, min_value))
        heapq.heappush(min_heap, (max_value, max_value))
    print(max_heap[0][1])