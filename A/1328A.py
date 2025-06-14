t = int(input())


for _ in range(t):
    a_and_b = [int(i) for i in str(input()).split(" ")]
    a = a_and_b[0]
    b = a_and_b[1]

    if a % b == 0:
        print(0)
    elif b > a:
        print(b - a)
    else:
        print(b - (a % b))