n = int(input())
coins = [int(i) for i in str(input()).split(" ")]

half = sum(coins) // 2
amount = 0
total_coins = 0

while amount <= half:
    max_coin = max(coins)
    new_amount = max_coin + amount
    if new_amount > half:
        min_coin = min(coins)
        if min_coin + amount > half:
            amount += min_coin
            total_coins += 1
            coins.remove(min_coin)
            continue
    amount = new_amount
    total_coins += 1
    coins.remove(max_coin)

print(total_coins)