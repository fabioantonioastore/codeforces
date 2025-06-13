n = int(input())
answers = [int(i) for i in str(input()).split(" ")]

if 1 in answers:
    print("Hard")
else:
    print("Easy")