# Read input
with open("12/groups.in", "r") as f:
    input = [line.strip() for line in f.readlines()]

visited = set()
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
directions = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
]
corners = [directions[:3], directions[2:5], directions[4:7], directions[6:]]


def is_corner(c, c1, c2, c3):
    if c != c1 and c != c3:
        return True
    if c != c2 and c == c1 == c3:
        return True
    return False


def get_input(i, j):
    if i < 0 or j < 0 or i >= len(input) or j >= len(input[0]):
        return "@"
    return input[i][j]


def dfs(i, j):
    if (i, j) in visited:
        return 0, 0
    visited.add((i, j))
    curr_area = 1
    curr_double_sides = 0
    for a, b, c in corners:
        if is_corner(
            get_input(i, j),
            get_input(i + a[0], j + a[1]),
            get_input(i + b[0], j + b[1]),
            get_input(i + c[0], j + c[1]),
        ):
            curr_double_sides += 1

    for delta in deltas:
        ni, nj = i + delta[0], j + delta[1]
        if not (
            0 <= ni < len(input)
            and 0 <= nj < len(input[0])
            and input[ni][nj] != input[i][j]
            or ni < 0
            or nj < 0
            or ni >= len(input)
            or nj >= len(input[0])
        ):
            area, double_sides = dfs(ni, nj)
            curr_area += area
            curr_double_sides += double_sides
    return curr_area, curr_double_sides


ans = 0
for i, line in enumerate(input):
    for j, c in enumerate(line):
        if (i, j) not in visited:
            area, double_sides = dfs(i, j)
            print(c, area, double_sides)
            ans += double_sides * area

print(ans)
