# Read the input file
with open("15/box.in", "r") as file:
    lines = file.readlines()

# Parse the input file
instructions = ""
grid = []
for line in lines:
    if line.startswith("#"):
        grid.append(list(line.strip()))
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
    if grid[i + di][j + dj] == "O":
        # Keep moving until we hit a wall or found a empty cell
        nx, ny = i + di, j + dj
        while grid[nx][ny] == "O":
            nx, ny = nx + di, ny + dj
        if grid[nx][ny] == ".":
            # Swap position of closest box and empty cell
            grid[nx][ny] = "O"
            grid[i + di][j + dj] = "@"
            grid[i][j] = "."
            start = (i + di, j + dj)
    else:
        grid[i + di][j + dj] = "@"
        grid[i][j] = "."
        start = (i + di, j + dj)

print_grid()

total_gps = 0
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "O":
            total_gps += 100 * i + j

print(total_gps)
