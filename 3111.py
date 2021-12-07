def replaced_right(original, old, new):
    text = original
    ridx = text.rindex(old)
    text = text[:ridx] + new + text[ridx+len(old):]
    return text


A = input()
T = input()
left = True
while T.count(A):
    if left:
        T = T.replace(A, '', 1)
    else:
        T = replaced_right(T, A, '')
    left = not left

print(T)