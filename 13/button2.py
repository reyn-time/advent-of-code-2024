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
            10000000000000 + int(prize.group(1)),
            10000000000000 + int(prize.group(2)),
        )

        # Try to find a, b such that a*AX + b*BX = PX and a*AY + b*BY = PY
        a = (PX * BY - PY * BX) / (AX * BY - AY * BX)
        b = (PX * AY - PY * AX) / (BX * AY - BY * AX)
        if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
            total += int(a) * 3 + int(b)


print(total)
