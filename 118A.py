string = str(input()).lower()

new_string = ""

consonants = ("a", "e", "i", "o", "u", "y")
for char in string:
    if char in consonants:
        continue
    new_string += "." + char

print(new_string)