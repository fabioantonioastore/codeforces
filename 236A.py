nickname = str(input())
letters = set(nickname)

if len(letters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")