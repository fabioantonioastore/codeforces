n = int(input())
pangram = str(input()).lower()

if len(set(pangram)) >= 26:
    print("YES")
else:
    print("NO")