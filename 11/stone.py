# Read input
with open("11/stone.in", "r") as f:
    input = list(map(int, f.readline().split()))


def transform(stone):
    if stone == 0:
        return [1]
    s_stone = str(stone)
    s_stone_len = len(s_stone)
    if s_stone_len % 2 == 0:
        return [int(s_stone[: s_stone_len // 2]), int(s_stone[s_stone_len // 2 :])]
    return [stone * 2024]


stones = {}
for stone in input:
    stones[stone] = stones.get(stone, 0) + 1

# Part 2: Change 25 to 75
for _ in range(25):
    next_stones = {}
    for stone, count in stones.items():
        for next_stone in transform(stone):
            next_stones[next_stone] = next_stones.get(next_stone, 0) + count
    stones = next_stones

print(sum(stones.values()))
