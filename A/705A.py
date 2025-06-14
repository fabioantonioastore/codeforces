n = int(input())

final_phrase_one = "I hate it"
final_phrase_two = "I love it"
phrase_one = "I hate that"
phrase_two = "I love that"
result = ""
if n == 1:
    print(final_phrase_one)
elif n == 2:
    print(phrase_one + " " + final_phrase_two)
else:
    swap = False
    for _ in range(n - 1):
        if swap:
            result += phrase_two + " "
            swap = False
            continue
        result += phrase_one + " "
        swap = True
    if n % 2 == 0:
        result += final_phrase_two
    else:
        result += final_phrase_one

print(result)