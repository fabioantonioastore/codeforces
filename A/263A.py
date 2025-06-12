matrix = []

for _ in range(5):
    line = [int(i) for i in str(input()).split(" ")]
    matrix.append(line)


def get_one_position() -> tuple:
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                return (i + 1, j + 1)
    raise "There is no 1"

matrix_position = get_one_position()
total_moves = abs(3 - matrix_position[0]) + abs(3 - matrix_position[1])
print(total_moves)