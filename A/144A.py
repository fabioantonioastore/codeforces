n = int(input())
soldiers = [int(i) for i in str(input()).split(" ")]


def get_min_soldier_index() -> int:
    min_soldier = 101
    min_index = 0
    for i in range(n):
        if soldiers[i] <= min_soldier:
            min_soldier = soldiers[i]
            min_index = i
    return min_index


def get_max_soldier_index() -> int:
    max_soldier = 0
    max_index = 0
    for i in range(n):
        if soldiers[i] > max_soldier:
            max_soldier = soldiers[i]
            max_index = i
    return max_index


max_index = get_max_soldier_index()
max_soldier = soldiers[max_index]
seconds = 0

while soldiers[0] != max_soldier:
    (soldiers[max_index], soldiers[max_index - 1]) = (soldiers[max_index - 1], soldiers[max_index])
    max_index -= 1
    seconds += 1

min_index = get_min_soldier_index()
min_soldier = soldiers[min_index]

while soldiers[-1] != min_soldier:
    (soldiers[min_index], soldiers[min_index + 1]) = (soldiers[min_index + 1], soldiers[min_index])
    min_index += 1
    seconds += 1

print(seconds)