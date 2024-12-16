# Read the input
with open("09/fragment.in", "r") as file:
    line = file.read().strip()

blocks = []
for i, c in enumerate(line):
    val = int(c)
    if i % 2 == 0:
        # Block
        for j in range(val):
            blocks.append(i // 2)
    else:
        # Hole
        for j in range(val):
            blocks.append(None)

l = 0
r = len(blocks) - 1
while l < r:
    if blocks[l] is None:
        blocks[l], blocks[r] = blocks[r], blocks[l]
        r -= 1
    else:
        l += 1

total = 0
for i, val in enumerate(blocks):
    if val is None:
        break
    total += val * i

print(total)
