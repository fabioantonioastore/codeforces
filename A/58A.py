word = str(input())

new_word = ""
for letter in word:
    if letter == "h" and not "h" in new_word and len(new_word) == 0:
        new_word += "h"
        continue
    if letter == "e" and not "he" in new_word and len(new_word) == 1:
        new_word += "e"
        continue
    if letter == "l" and not "hel" in new_word and len(new_word) == 2:
        new_word += "l"
        continue
    if letter == "l" and not "hell" in new_word and len(new_word) == 3:
        new_word += "l"
        continue
    if letter == "o" and not "hello" in new_word and len(new_word) == 4:
        new_word += "o"
        break

if new_word == "hello":
    print("YES")
else:
    print("NO")