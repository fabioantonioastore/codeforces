number = str(input())

lucky_numbers = (4, 7)

if number.count("4") + number.count("7") in lucky_numbers:
    print("YES")
else:
    print("NO")