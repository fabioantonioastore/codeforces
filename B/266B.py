first_inputs = [int(i) for i in str(input()).split(" ")]
n = first_inputs[0]
times = first_inputs[1]

queue = [children for children in str(input())]
for t in range(times):
    i = 0
    next_i = 1
    while True:
        if next_i > n - 1:
            break
        if queue[i] == "B" and queue[next_i] == "G":
            (queue[i], queue[next_i]) = (queue[next_i], queue[i])
            i += 2
            next_i += 2
        else:
            i += 1
            next_i += 1

queue_string = ""
for children in queue:
    queue_string += children

print(queue_string)