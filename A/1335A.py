t = int(input())

for _ in range(t):
    n = int(input())
    total_ways = None
    if n % 2 == 0:
        total_ways = (n // 2) - 1
    else:
        total_ways = ((n + 1) // 2) - 1

    print(total_ways)