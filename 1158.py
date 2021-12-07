N, K = map(int, input().split())
people = [i for i in range(1, N+1)]
key = 0
temp = K - 1
order = []
while people:
    key = (key+temp) % len(people)
    order.append(people.pop(key))
print('<'+', '.join(map(str, order))+'>')
