# Read the maze from the file
with open("20/cheat.in", "r") as file:
    maze = [line.strip() for line in file.readlines()]

start = None
end = None
for i, row in enumerate(maze):
    for j, cell in enumerate(row):
        if cell == "S":
            start = (i, j)
        elif cell == "E":
            end = (i, j)

cost = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]

curr = start
prev = None
path = []
while curr != end:
    cx, cy = curr
    path.append(curr)
    cost[cx][cy] = len(path)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if maze[cx + dx][cy + dy] == "#":
            continue
        if (cx + dx, cy + dy) == prev:
            continue
        prev = curr
        curr = (cx + dx, cy + dy)
        break
cost[end[0]][end[1]] = len(path) + 1

# Try all routes with manhattan distance <= 20
skips = []
for i in range(21):
    for j in range(21 - i):
        if i + j <= 1:
            continue
        skips.append((i, j))
        if j != 0:
            skips.append((i, -j))
        if i != 0:
            skips.append((-i, j))
            if j != 0:
                skips.append((-i, -j))

useful_cheat_count = 0
# Try all types of cheats
for cx, cy in path:
    for dx, dy in skips:
        if (
            0 <= cx + dx < len(maze)
            and 0 <= cy + dy < len(maze[0])
            and cost[cx + dx][cy + dy] - cost[cx][cy] - abs(dx) - abs(dy) > 0
        ):
            cost_saved = cost[cx + dx][cy + dy] - cost[cx][cy] - abs(dx) - abs(dy)
            if cost_saved >= 100:
                useful_cheat_count += 1

print(useful_cheat_count)
