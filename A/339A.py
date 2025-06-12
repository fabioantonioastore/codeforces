numbers = [int(i) for i in str(input()).split("+")]
numbers.sort()

result = ""
for number in numbers:
    result += str(number) + "+"
print(result[0:-1:])