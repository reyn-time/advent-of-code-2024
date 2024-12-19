# Read the input file
with open("15/box.in", "r") as file:
    lines = file.readlines()

# Parse the input file
instructions = ""
grid = []
for line in lines:
    if line.startswith("#"):
        grid_line = []
        for cell in line.strip():
            if cell == "." or cell == "#":
                grid_line.append(cell)
                grid_line.append(cell)
            elif cell == "O":
                grid_line.append("[")
                grid_line.append("]")
            else:
                grid_line.append(cell)
                grid_line.append(".")
        grid.append(grid_line)
    else:
        instructions += line.strip()

# Find the starting position
start = None
for i, row in enumerate(grid):
    if start is not None:
        break
    for j, cell in enumerate(row):
        if cell == "@":
            start = (i, j)
            break

command_to_delta = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}


def print_grid():
    for row in grid:
        print("".join(row))


for command in instructions:
    i, j = start
    di, dj = command_to_delta[command]
    if grid[i + di][j + dj] == "#":
        continue
    if grid[i + di][j + dj] in "[]":
        if di == 0:
            nj = j + dj
            while grid[i][nj] in "[]":
                nj += dj
            if grid[i][nj] == ".":
                while nj != j:
                    grid[i][nj], grid[i][nj - dj] = grid[i][nj - dj], grid[i][nj]
                    nj -= dj
                start = (i, j + dj)
        else:
            # Recursive push box hell
            line = set()
            if grid[i + di][j] == "[":
                line = {j, j + 1}
            else:
                line = {j - 1, j}
            stack = [line]
            can_push = True
            while can_push:
                next_line = set()
                for elem in stack[-1]:
                    if grid[i + di * (len(stack) + 1)][elem] == "[":
                        next_line.add(elem)
                        next_line.add(elem + 1)
                    elif grid[i + di * (len(stack) + 1)][elem] == "]":
                        next_line.add(elem)
                        next_line.add(elem - 1)
                    elif grid[i + di * (len(stack) + 1)][elem] == "#":
                        can_push = False
                        break

                if len(next_line) > 0:
                    stack.append(next_line)
                else:
                    break
            if can_push:
                for offset, s in reversed(list(enumerate(stack))):
                    for elem in s:
                        (
                            grid[i + di * (offset + 1)][elem],
                            grid[i + di * (offset + 2)][elem],
                        ) = (
                            grid[i + di * (offset + 2)][elem],
                            grid[i + di * (offset + 1)][elem],
                        )
                grid[i][j] = "."
                start = (i + di, j + dj)
                grid[i + di][j + dj] = "@"

    else:
        grid[i + di][j + dj] = "@"
        grid[i][j] = "."
        start = (i + di, j + dj)

total_gps = 0
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "[":
            total_gps += 100 * i + j

print(total_gps)
