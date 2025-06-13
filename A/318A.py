inputs = [int(i) for i in str(input()).split(" ")]
n = inputs[0]
k = inputs[1]

number = None
if n % 2 == 0:
    if k > n / 2:
        number = 2 * (k - (n // 2))
    else:
        number = 1 + (2 * (k - 1))
else:
    if k > (n // 2) + 1:
        number = 2 * (k - ((n // 2) + 1))
    else:
        number = 1 + (2 * (k - 1))

print(number)