N = int(input())

for _ in range(N):
    word = input()
    char_dict = dict()
    for i in range(len(char_dict)):
        if i == 0:
            char_dict[word[i]] = 1

