import re

# Read input from file
with open("03/mul.in", "r") as file:
    input = file.read().strip()

# Merge enables and disables and sort by start index
enables = [(m.start(), True) for m in re.finditer(r"do\(\)", input)]
disables = [(m.start(), False) for m in re.finditer(r"don't\(\)", input)]
events = sorted(enables + disables, key=lambda x: x[0])
i = 0

total = 0
for m in re.finditer(r"mul\((\d+),(\d+)\)", input):
    # Find the event that occurs before the current match
    while i < len(events) and events[i][0] < m.start():
        i += 1

    # If the event is an enable, add the product to the total
    if i == 0 or (i > 0 and events[i - 1][1]):
        print(m.group(1), m.group(2))
        total += int(m.group(1)) * int(m.group(2))

print(total)
