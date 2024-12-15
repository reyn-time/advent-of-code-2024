import re

# Read input from file
with open("03/mul.in", "r") as file:
    input = file.read().strip()


total = 0
for a, b in re.findall(r"mul\((\d+),(\d+)\)", input):
    total += int(a) * int(b)

print(total)
