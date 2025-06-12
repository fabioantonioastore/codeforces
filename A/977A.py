inputs = str(input()).split(" ")
n = int(inputs[0])
k = int(inputs[1])

for _ in range(k):
    if n % 10 == 0:
        n //= 10
    else:
        n -= 1

print(n)