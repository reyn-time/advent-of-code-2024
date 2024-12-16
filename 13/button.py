import re

# Read input
with open("13/button.in", "r") as f:
    input = f.readlines()

regex = re.compile(f"X\+(\d+), Y\+(\d+)")
regex_prize = re.compile(f"X=(\d+), Y=(\d+)")

# Process input
total = 0
for i, line in enumerate(input):
    if i % 4 == 0:
        button_a = regex.search(line)
    elif i % 4 == 1:
        button_b = regex.search(line)
    elif i % 4 == 2:
        prize = regex_prize.search(line)
        AX, AY, BX, BY, PX, PY = (
            int(button_a.group(1)),
            int(button_a.group(2)),
            int(button_b.group(1)),
            int(button_b.group(2)),
            int(prize.group(1)),
            int(prize.group(2)),
        )

        # Try to find a, b such that a*AX + b*BX = PX and a*AY + b*BY = PY
        min_cost = float("inf")
        for a in range(PX // AX + 1):
            remainderX = (PX - a * AX) % BX
            remainderY = (PY - a * AY) % BY
            if (
                remainderX == 0
                and remainderY == 0
                and (PX - a * AX) // BX == (PY - a * AY) // BY
            ):
                min_cost = min(min_cost, a * 3 + (PX - a * AX) // BX)

        if min_cost != float("inf"):
            total += min_cost

print(total)
