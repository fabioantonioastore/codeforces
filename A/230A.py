inputs = [int(i) for i in str(input()).split(" ")]

kirito = inputs[0]
total_dragons = inputs[1]


class Dragon:
    def __init__(self, x: int, y: int) -> None:
        self.strenght = x
        self.bonus = y



def get_min_dragon(dragons: list[Dragon]) -> Dragon:
    min_dragon = dragons[0]
    for i in range(1, len(dragons)):
        if dragons[i].strenght < min_dragon.strenght:
            min_dragon = dragons[i]
    return min_dragon


dragons = []
for _ in range(total_dragons):
    dragon = [int(i) for i in str(input()).split(" ")]
    dragons.append(Dragon(dragon[0], dragon[1]))

possible = True
while len(dragons) != 0:
    min_dragon = get_min_dragon(dragons)
    if kirito <= min_dragon.strenght:
        possible = False
        break
    kirito += min_dragon.bonus
    dragons.remove(min_dragon)

if possible:
    print("YES")
else:
    print("NO")