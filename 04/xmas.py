# Read input from file
with open("04/xmas.in", "r") as file:
    input = file.read().strip()

# Split input into lines
lines = [line.strip() for line in input.split("\n")]

# Print the lines
to_search = []

rows = len(lines)
cols = len(lines[0])

# Horizontal
for line in lines:
    to_search.append(line)
    to_search.append(line[::-1])

# Vertical
for i in range(cols):
    s = "".join([line[i] for line in lines])
    to_search.append(s)
    to_search.append(s[::-1])

# Diagonal
d = {}
for i in range(rows):
    for j in range(cols):
        d[i - j] = d.get(i - j, "") + lines[i][j]

for k in d:
    to_search.append(d[k])
    to_search.append(d[k][::-1])

# Anti-diagonal
d = {}
for i in range(rows):
    for j in range(cols):
        d[i + j] = d.get(i + j, "") + lines[i][j]

for k in d:
    to_search.append(d[k])
    to_search.append(d[k][::-1])

print(sum(line.count("XMAS") for line in to_search))
