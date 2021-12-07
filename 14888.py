from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
min_value = 1000000000
max_value = -1000000000
op_dict = {0: '+', 1: '-', 2: '*', 3:'/'}
ops = []
for idx, op_cnt in enumerate(list(map(int, input().split()))):
    ops.extend([op_dict[idx]] * op_cnt)
for op_per in set(permutations(ops, N-1)):
    result = nums[0]
    for i in range(N-1):
        op = op_per[i]
        num = nums[i+1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            result = -(-result // num) if result < 0 else result // num
    min_value = min(min_value, result)
    max_value = max(max_value, result)
print(max_value)
print(min_value)