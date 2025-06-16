n = int(input())

database = dict()

for _ in range(n):
    name = str(input())
    if not name in database:
        database[name] = [name]
        print("OK")
        continue
    if name == database[name][-1]:
        database[name].append(name + str(1))
        print(database[name][-1])
        continue
    name_len = len(name)
    count = int(database[name][-1][name_len::]) + 1
    new_name = name + str(count)
    database[name].append(new_name)
    print(new_name)