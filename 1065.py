def solution(n):
    str_n = str(n)
    diff = None

    for j in range(1, len(str_n)):
        if diff is not None:
            if int(str_n[j - 1]) - int(str_n[j]) != diff:
                return False
        else:
            diff = int(str_n[j - 1]) - int(str_n[j])

    return True


N = int(input())
result = 0
for i in range(1, N+1):
    if solution(i):
        result += 1
print(result)