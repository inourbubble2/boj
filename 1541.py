exp = list(input().split('-'))
value = 0
for num in exp[0].split('+'):
    value += int(num)
for minus_num in exp[1:]:
    for plus_num in minus_num.split('+'):
        value -= int(plus_num)
print(value)