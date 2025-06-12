n = int(input())
stones = str(input())

total = 0
prev_stone = ""
for stone in stones:
    if stone == prev_stone:
        total += 1
    else:
        prev_stone = stone

print(total)