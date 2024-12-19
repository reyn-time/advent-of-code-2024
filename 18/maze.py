# Read the maze.in file.
import heapq

grid_length = 70
obstacle_count = 1024

with open("18/maze.in", "r") as file:
    obstacles = set(
        [tuple(map(int, line.strip().split(","))) for line in file.readlines()][
            :obstacle_count
        ]
    )

curr = (0, 0)
min_for_nodes = {}
heap = [(0, curr)]

while heap:
    cost, curr = heapq.heappop(heap)
    if curr in min_for_nodes and min_for_nodes[curr] <= cost:
        continue
    min_for_nodes[curr] = cost
    if curr == (grid_length, grid_length):
        break
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next = (curr[0] + dx, curr[1] + dy)
        if (
            0 <= next[0] <= grid_length
            and 0 <= next[1] <= grid_length
            and next not in obstacles
        ):
            heapq.heappush(heap, (cost + 1, next))

print(min_for_nodes[(grid_length, grid_length)])
