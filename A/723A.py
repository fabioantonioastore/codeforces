distances = [int(i) for i in str(input()).split(" ")]

a = distances[0]
b = distances[1]
c = distances[2]

print(min(
    abs(a - b) + abs(a - c),
    abs(b - a) + abs(b - c),
    abs(c - a) + abs(c - b)
))