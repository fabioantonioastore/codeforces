a = int(input())
b = int(input())
c = int(input())

max_value = 0

result = None
if a == b == c == 1:
    result = a + b + c
elif a == b == 1:
    result = (a + b) * c
elif a == c == 1:
    result = a + b + c
elif b == c == 1:
    result = a * (b + c)
elif a == 1:
    result = (a + b) * c
elif b == 1:
    if a > c:
        result = a * (b + c)
    else:
        result = (a + b) * c
elif c == 1:
    result = a * (b + c)
else:
    result = a * b * c

print(result)