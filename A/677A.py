inputs = [int(i) for i in str(input()).split(" ")]
n = inputs[0]
h = inputs[1]

heights = [int(i) for i in str(input()).split(" ")]
minimum_road_size = 0

for person in heights:
    if person > h:
        minimum_road_size += 2
        continue
    minimum_road_size += 1

print(minimum_road_size)