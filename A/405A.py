n = int(input())
columns = [int(i) for i in str(input()).split(" ")]

columns.sort()
new_column = ""
for column in columns:
    new_column += str(column) + " "

print(new_column)