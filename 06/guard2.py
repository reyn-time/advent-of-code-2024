# Read the input file
with open("06/guard.in", "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]

# Find current position, i.e. the first '^'
curr_x, curr_y = None, None
for i, line in enumerate(lines):
    if "^" in line:
        curr_x, curr_y = (i, line.index("^"))
        break

deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_path(lines, curr_x, curr_y):
    direction = 0
    visited = set()
    while 0 <= curr_x < len(lines) and 0 <= curr_y < len(lines[0]):
        if (curr_x, curr_y) not in visited:
            visited.add((curr_x, curr_y))

        delta_x, delta_y = deltas[direction]
        next_x, next_y = curr_x + delta_x, curr_y + delta_y
        if (
            0 <= next_x < len(lines)
            and 0 <= next_y < len(lines[0])
            and lines[next_x][next_y] == "#"
        ):
            direction = (direction + 1) % 4
        else:
            curr_x, curr_y = next_x, next_y

    return visited


def has_cycle(lines, curr_x, curr_y):
    direction = 0
    visited = set()

    while 0 <= curr_x < len(lines) and 0 <= curr_y < len(lines[0]):
        if (curr_x, curr_y, direction) in visited:
            return True
        visited.add((curr_x, curr_y, direction))

        delta_x, delta_y = deltas[direction]
        next_x, next_y = curr_x + delta_x, curr_y + delta_y
        if (
            0 <= next_x < len(lines)
            and 0 <= next_y < len(lines[0])
            and lines[next_x][next_y] == "#"
        ):
            direction = (direction + 1) % 4
        else:
            curr_x, curr_y = next_x, next_y

    return False


count = 0
for cell_x, cell_y in get_path(lines, curr_x, curr_y):
    if cell_x == curr_x and cell_y == curr_y:
        continue

    lines[cell_x][cell_y] = "#"
    if has_cycle(lines, curr_x, curr_y):
        count += 1
    lines[cell_x][cell_y] = "."

print(count)
