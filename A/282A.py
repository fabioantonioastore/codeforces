n = int(input())
x = 0
for _ in range(n):
    command = str(input())
    if "+" in command:
        x += 1
    else:
        x -= 1
print(x)