n = int(input())
segment = [int(i) for i in str(input()).split(" ")]

subsegment = 0
max_subsegment_len = 0
subsegment_len = 0
for a in segment:
    if a >= subsegment:
        subsegment = a
        subsegment_len += 1
        if subsegment_len > max_subsegment_len:
            max_subsegment_len = subsegment_len
        continue
    subsegment = a
    subsegment_len = 1

print(max_subsegment_len)