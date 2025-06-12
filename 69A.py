n = int(input())
final_body = [0, 0, 0]
for _ in range(n):
    body = [int(i) for i in str(input()).split(" ")]
    final_body[0] += body[0]
    final_body[1] += body[1]
    final_body[2] += body[2]

if set(final_body) == {0}:
    print("YES")
else:
    print("NO")