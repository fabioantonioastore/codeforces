word = str(input())

new_word = ""
if word.isupper():
    new_word = word.lower()
elif len(word) == 1 and word.islower():
    new_word = word.upper()
elif word[0].islower() and word[1::].isupper():
    new_word += word[0].upper() + word[1::].lower()
else:
    new_word = word

print(new_word)