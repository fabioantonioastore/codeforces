first_input = str(input()).split(" ")
n = int(first_input[0])
k = int(first_input[1])

second_input = [int(i) for i in str(input()).split(" ")]

total_passed = 0

prev_score = 0
for i in range(n):
    score = second_input[i]
    if score == 0:
        break
    if score != prev_score and total_passed >= k:
        break
    prev_score = score
    total_passed += 1

print(total_passed)