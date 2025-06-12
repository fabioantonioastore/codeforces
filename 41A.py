word = str(input())
reverse_word = str(input())

answer = True
if len(word) != len(reverse_word):
    answer = False
else:
    for i in range(len(word)):
        if word[i] != reverse_word[-1 - i]:
            answer = False
            break

if answer:
    print("YES")
else:
    print("NO")