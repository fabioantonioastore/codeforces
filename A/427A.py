n = int(input())
events = [int(i) for i in str(input()).split(" ")]

total_officers = 0
untreated = 0
for event in events:
    if total_officers == 0 and event == -1:
        untreated += 1
        continue
    if event == -1:
        total_officers -= 1
        continue
    total_officers += event

print(untreated)