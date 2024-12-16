# Read the input
with open("09/fragment.in", "r") as file:
    line = file.read().strip()

blocks = []  # (length, pos)
holes = []  # (length, pos)
pos = 0

for i, c in enumerate(line):
    val = int(c)
    if i % 2 == 0:
        blocks.append((val, pos))
    elif val > 0:
        holes.append((val, pos))
    pos += val

for i, (block_length, block_pos) in reversed(list(enumerate(blocks))):
    found_j = None
    for j, (hole_length, hole_pos) in enumerate(holes):
        if block_pos < hole_pos:
            break
        if hole_length >= block_length:
            found_j = j
            break
    if found_j is not None:
        blocks[i] = (block_length, hole_pos)
        holes[found_j] = (hole_length - block_length, hole_pos + block_length)

checksum = 0
for i, (block_length, block_pos) in enumerate(blocks):
    checksum += i * (block_pos * 2 + block_length - 1) * block_length // 2

print(checksum)
