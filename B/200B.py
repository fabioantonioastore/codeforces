n = int(input())
inputs = [int(i) for i in str(input()).split(" ")]

orange_juice_percentage = 0
for i in inputs:
    orange_juice_percentage += i

print(orange_juice_percentage / n)