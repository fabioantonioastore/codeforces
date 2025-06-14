horseshoes = [int(i) for i in str(input()).split()]

result = 4 - len(set(horseshoes))
print(result)