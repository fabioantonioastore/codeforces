n = int(input())

total_available_rooms = 0
for _ in range(n):
    room = [int(i) for i in str(input()).split(" ")]
    if room[1] - room[0] >= 2:
        total_available_rooms += 1
        continue

print(total_available_rooms)