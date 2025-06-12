word = str(input())
word_len = len(word)
uppercase_letters = 0

for letter in word:
    if letter == letter.upper():
        uppercase_letters += 1

if uppercase_letters > word_len / 2:
    word = word.upper()
else:
    word = word.lower()

print(word)