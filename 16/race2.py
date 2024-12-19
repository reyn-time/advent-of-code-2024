# Read input
import heapq


with open("16/race.in", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

# Find start
start = None
for i, row in enumerate(grid):
    if start is not None:
        break
    for j, cell in enumerate(row):
        if cell == "S":
            start = (i, j)
            break

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
curr_dir = 0

best_cost_for_node_and_dir = {}
heap = [(0, start, curr_dir, None)]
best_cost = float("inf")

while heap:
    cost, curr, curr_dir, last_move = heapq.heappop(heap)
    if (curr, curr_dir) in best_cost_for_node_and_dir and best_cost_for_node_and_dir[
        (curr, curr_dir)
    ][0] < cost:
        continue

    prev_cost, prev_moves = best_cost_for_node_and_dir.get(
        (curr, curr_dir), (float("inf"), [])
    )
    prev_moves.append(last_move)
    best_cost_for_node_and_dir[(curr, curr_dir)] = (cost, prev_moves)
    if cost == prev_cost:
        continue

    # Check if we've reached the end
    if grid[curr[0]][curr[1]] == "E":
        best_cost = min(best_cost, cost)
        continue

    # Relax edges: Forward
    dx, dy = directions[curr_dir]
    nx, ny = curr[0] + dx, curr[1] + dy
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
        heapq.heappush(heap, (cost + 1, (nx, ny), curr_dir, "forward"))

    # Relax edges: Turn left
    left_dir = (curr_dir - 1) % 4
    heapq.heappush(heap, (cost + 1000, curr, left_dir, "left"))

    # Relax edges: Turn right
    right_dir = (curr_dir + 1) % 4
    heapq.heappush(heap, (cost + 1000, curr, right_dir, "right"))

# Find the end position
end = None
for i, row in enumerate(grid):
    if end is not None:
        break
    for j, cell in enumerate(row):
        if cell == "E":
            end = (i, j)
            break

queue = []
for dir in range(4):
    if (end, dir) in best_cost_for_node_and_dir and best_cost_for_node_and_dir[
        (end, dir)
    ][0] == best_cost:
        queue.append((end, dir))

visited = set()
while queue:
    curr, dir = queue.pop(0)
    visited.add((curr))
    moves = best_cost_for_node_and_dir[(curr, dir)][1]
    for move in moves:
        if move == "forward":
            dx, dy = directions[dir]
            prev = (curr[0] - dx, curr[1] - dy)
            queue.append((prev, dir))
        elif move == "left":
            dir = (dir + 1) % 4
            queue.append((curr, dir))
        elif move == "right":
            dir = (dir - 1) % 4
            queue.append((curr, dir))

print(len(visited))
