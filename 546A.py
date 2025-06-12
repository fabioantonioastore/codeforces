inputs = [int(i) for i in str(input()).split(" ")]
k = inputs[0]
n = inputs[1]
w = inputs[2]

total = 0
for i in range(1, w + 1):
    total += i * k

if total <= n:
    total = 0
else:
    total -= n

print(total)