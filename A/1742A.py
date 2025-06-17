t = int(input())

for _ in range(t):
    numbers = [int(i) for i in str(input()).split(" ")]
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]

    if (
        a + b == c or
        a + c == b or
        c + b == a
    ):
        print("YES")
        continue
    print("NO")