problem_input = [int(i) for i in str(input()).split(" ")]
n = problem_input[0]
m = problem_input[1]
a = problem_input[2]

total = 1

if a == 1:
    total = n * m
else:
    if n > a:
        total = n // a
        if n % a > 0:
            total += 1
    if m > a:
        times = m // a
        if m % a > 0:
            times += 1
        total *= times

print(total)