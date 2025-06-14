n = int(input())
p_indices = [int(i) for i in  str(input()).split(" ")]
q_indices = [int(i) for i in str(input()).split(" ")]

p_q_set = set(p_indices[1::])
p_q_set.update(q_indices[1::])
p_q_set = sorted(p_q_set)

level = 1
can_pass = True
if len(p_q_set) >= n:
    for l in p_q_set:
        if level != l:
            can_pass = False
            break
        level += 1
else:
    can_pass = False

if can_pass:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")