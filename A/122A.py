from typing import Generator


number = int(input())

def is_lucky_number(n: int) -> bool:
    n_set = set(str(n))
    if len(n_set) == 1:
        return "4" in n_set or "7" in n_set
    return n_set == {"4", "7"}


def gen_lucky_number(n: int) -> Generator:
    for i in range(1, n):
        if is_lucky_number(i):
            yield i


if is_lucky_number(number):
    print("YES")
else:
    is_almost_lucky = False
    for lucky in gen_lucky_number(number):
        if number % lucky == 0:
            is_almost_lucky = True
            break
    if is_almost_lucky:
        print("YES")
    else:
        print("NO")