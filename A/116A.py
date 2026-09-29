n = int(input())

total_passengers = 0
max_passengers = 0

for _ in range(n):
    inputs = [int(i) for i in str(input()).split(" ")]
    a = inputs[0]
    b = inputs[1]

    total_passengers = total_passengers - a + b
    if total_passengers > max_passengers:
        max_passengers = total_passengers

print(max_passengers)