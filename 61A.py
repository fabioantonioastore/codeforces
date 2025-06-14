first_number = str(input())
second_number = str(input())

result = ""

for i in range(len(first_number)):
    if first_number[i] == second_number[i]:
        result += "0"
        continue
    result += "1"

print(result)