t = int(input())

for _ in range(t):
    n = int(input())

    digits = 1
    k = 1
    number = ""
    while n // (10 ** digits) > 0:
        rest = n % (10 ** digits)
        digits += 1
        n -= rest
        if rest != 0:
            k += 1
            number += str(rest) + " "
    number += str(n)
    print(k)
    print(number)