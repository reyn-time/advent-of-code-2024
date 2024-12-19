grid_length = 70

# Fill the maze with obstacles, and remove them until the maze is solvable.
with open("18/maze.in", "r") as file:
    obstacles = [tuple(map(int, line.strip().split(","))) for line in file.readlines()]

s = set(obstacles)

parent = {
    (x, y): (x, y) for x in range(grid_length + 1) for y in range(grid_length + 1)
}


# Disjoint set
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[find(x)] = find(y)


def is_connected(x, y):
    return find(x) == find(y)


moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(grid_length + 1):
    for j in range(grid_length + 1):
        if (i, j) in s:
            continue
        for dx, dy in moves:
            if (
                0 <= i + dx <= grid_length
                and 0 <= j + dy <= grid_length
                and (i + dx, j + dy) not in s
            ):
                union((i, j), (i + dx, j + dy))

i = len(obstacles) - 1
while not is_connected((0, 0), (grid_length, grid_length)):
    x, y = obstacles[i]
    s.remove((x, y))
    for dx, dy in moves:
        if (
            0 <= x + dx <= grid_length
            and 0 <= y + dy <= grid_length
            and (x + dx, y + dy) not in s
        ):
            union((x, y), (x + dx, y + dy))
    i -= 1

print(obstacles[i + 1])
