n = int(input())
for _ in range(n):
    word = str(input())
    word_size = len(word)
    if word_size > 10:
        word = word[0] + str(word_size - 2) + word[-1]
    print(word)