first_word = str(input())
second_word = str(input())
third_word = [i for i in str(input())]

possible = True
for letter in first_word:
    try:
        third_word.remove(letter)
    except:
        possible = False
        break

if possible:
    for letter in second_word:
        try:
            third_word.remove(letter)
        except:
            possible = False
            break

if possible and len(third_word) == 0:
    print("YES")
else:
    print("NO")