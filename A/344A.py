n = int(input())

groups = 1
previous_magnet_end = ""
for _ in range(n):
    magnet = [i for i in str(input())]
    if magnet[0] == previous_magnet_end:
        groups += 1
    previous_magnet_end = magnet[1]

print(groups)