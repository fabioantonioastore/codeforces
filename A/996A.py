withdraw = int(input())

bills = {
    4: 1,
    3: 5,
    2: 10,
    1: 20,
    0: 100
}

total_bills = 0
for i in range(5):
    total_bills += withdraw // bills[i]
    withdraw = withdraw % bills[i]

print(total_bills)