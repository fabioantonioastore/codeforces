inputs = [int(i) for i in str(input()).split(" ")]
n = inputs[0]
m = inputs[1]

swap = False
for i in range(n):
    if i % 2 == 0:
        print("#" * m)
        continue
    if swap:
        print("#" + "." * (m - 1))
    else:
        print("." * (m - 1) + "#")
    swap = not swap