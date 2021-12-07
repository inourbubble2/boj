a = input()
b = input()

res = 0
cnt = 1
for i in range(2, -1, -1):
    print(int(a) * int(b[i]))
    res += int(a) * int(b[i]) * cnt
    cnt *= 10
print(res)
