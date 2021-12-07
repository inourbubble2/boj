equals = {}
notequals = {}
S = input()
for s in S.split('&&'):
    if '==' in s:
        a, b = s.split('==')
        if b.isalpha():
            pass
    elif '!=' in s:
        a, b = s.split('!=')
        notequals[a] = b
print(equals)
print(notequals)