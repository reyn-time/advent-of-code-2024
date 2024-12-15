# Read the input file
with open("06/guard.in", "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]

# Find current position, i.e. the first '^'
curr_x, curr_y = None, None
for i, line in enumerate(lines):
    if "^" in line:
        curr_x, curr_y = (i, line.index("^"))
        break

direction = 0
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
x_count = 0
while 0 <= curr_x < len(lines) and 0 <= curr_y < len(lines[0]):
    if lines[curr_x][curr_y] != "X":
        x_count += 1
        lines[curr_x][curr_y] = "X"

    next_x, next_y = curr_x + deltas[direction][0], curr_y + deltas[direction][1]
    if (
        0 <= next_x < len(lines)
        and 0 <= next_y < len(lines[0])
        and lines[next_x][next_y] == "#"
    ):
        direction = (direction + 1) % 4
    else:
        curr_x, curr_y = next_x, next_y

print(x_count)
