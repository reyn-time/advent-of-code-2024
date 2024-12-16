# Read input
with open("12/groups.in", "r") as f:
    input = [line.strip() for line in f.readlines()]

visited = set()
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(i, j):
    if (i, j) in visited:
        return 0, 0
    visited.add((i, j))
    curr_area = 1
    curr_perimeter = 0
    for delta in deltas:
        ni, nj = i + delta[0], j + delta[1]
        if (
            0 <= ni < len(input)
            and 0 <= nj < len(input[0])
            and input[ni][nj] != input[i][j]
            or ni < 0
            or nj < 0
            or ni >= len(input)
            or nj >= len(input[0])
        ):
            curr_perimeter += 1
        else:
            area, perimeter = dfs(ni, nj)
            curr_area += area
            curr_perimeter += perimeter
    return curr_area, curr_perimeter


ans = 0
for i, line in enumerate(input):
    for j, _ in enumerate(line):
        if (i, j) not in visited:
            area, perimeter = dfs(i, j)
            ans += perimeter * area

print(ans)
