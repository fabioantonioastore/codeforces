year = int(input())

i = 1
new_year = str(year + i)
while True:
    if len(set(new_year)) == 4:
        break
    i += 1
    new_year = str(year + i)

print(new_year)