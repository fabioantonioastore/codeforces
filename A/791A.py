weights = [int(i) for i in str(input()).split(" ")]

limak = weights[0]
bob = weights[1]

limak_year_factor = 3
bob_year_factor = 2

years = 0
while True:
    if limak > bob:
        break
    limak *= limak_year_factor
    bob *= bob_year_factor
    years += 1

print(years)