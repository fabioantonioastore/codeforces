n = int(input())
groups = [int(i) for i in str(input()).split(" ")]

one_group = groups.count(1)
two_group = groups.count(2)
three_group = groups.count(3)
total = groups.count(4)

if three_group >= one_group:
    three_group -= one_group
    total += one_group
    one_group = 0
elif one_group >= three_group:
    one_group -= three_group
    total += three_group
    three_group = 0

if two_group:
    total += two_group // 2
    rest_two_group = two_group % 2
    if rest_two_group:
        if one_group >= 2:
            one_group -= 2
        elif one_group == 1:
            one_group = 0
        total += 1

if three_group:
    total += three_group
if one_group:
    total += (one_group // 4)
    if one_group % 4:
        total += 1

print(total)