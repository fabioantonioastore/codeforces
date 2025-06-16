n = int(input())
numbers = [int(i) for i in str(input()).split(" ")]

even_number = True
if numbers[0] % 2 == 0 and (numbers[1] % 2 == 0 or numbers[2] % 2 == 0):
    even_number = False
elif numbers[1] % 2 == 0 and (numbers[0] % 2 == 0 or numbers[2] % 2 == 0):
    even_number = False
elif numbers[2] % 2 == 0 and (numbers[0] % 2 == 0 or numbers[1] % 2 == 0):
    even_number = False

result = None
for number in numbers:
    if even_number:
        if number % 2 == 0:
            result = numbers.index(number) + 1
            break
    else:
        if number % 2 != 0:
            result = numbers.index(number) + 1
            break

print(result)