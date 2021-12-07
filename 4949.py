def is_balanced(s):
    result = True
    stack = list()
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                result = False
        elif c == ']':
            if not stack or stack.pop() != '[':
                result = False
    if result and not stack:
        return 'yes'
    else:
        return 'no'


while True:
    s = input()
    if s == '.':
        break
    else:
        print(is_balanced(s))