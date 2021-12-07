import math


A, B, V = map(int, input().split(' '))
up = A - B
days = math.ceil((V - A) / up + 1)
print(days)

