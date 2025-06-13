n = int(input())

friends = [int(i) for i in str(input()).split(" ")]
result = [0 for _ in range(n)]

for i in range(n):
    index = friends.index(i + 1)
    result[i] = index + 1

string = ""
for r in result:
    string += str(r) + " "
print(string)