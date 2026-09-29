numbers = [int(n) for n in str(input()).split(" ")]
n = numbers[0]
k = numbers[1]
l = numbers[2]
c = numbers[3]
d = numbers[4]
p = numbers[5]
nl = numbers[6]
np = numbers[7]
result = min((k * l) // nl, c * d, p // np) // n
print(result)
