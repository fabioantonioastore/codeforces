n = int(input())
sequence = str(input())

a_counts = sequence.count("A")
d_counts = sequence.count("D")

if a_counts > d_counts:
    print("Anton")
elif a_counts < d_counts:
    print("Danik")
else:
    print("Friendship")