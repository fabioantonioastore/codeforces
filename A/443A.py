the_set = str(input())
new_set = set()

for letter in the_set:
    if not letter in "{}, ":
        new_set.add(letter)

print(len(new_set))