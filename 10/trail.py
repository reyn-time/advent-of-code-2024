from collections import deque

# Read input
with open("10/trail.in", "r") as f:
    lines = [[int(c) for c in line.strip()] for line in f.readlines()]


def score(i, j):
    visited = set()
    visited.add((i, j))
    queue = deque([(i, j)])
    total_score = 0
    while queue:
        x, y = queue.popleft()
        if lines[x][y] == 9:
            total_score += 1
            continue
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(lines)
                and 0 <= ny < len(lines[nx])
                and lines[nx][ny] == lines[x][y] + 1
                and (nx, ny) not in visited
            ):
                queue.append((nx, ny))
                visited.add((nx, ny))
    return total_score


total_score = 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == 0:
            total_score += score(i, j)
print(total_score)
