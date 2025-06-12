n = int(input())
total = 0
for _ in range(n):
    problem = str(input())
    if problem.count("1") > 1:
        total += 1
print(total)