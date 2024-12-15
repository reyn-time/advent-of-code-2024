# Read the input file
with open("08/antenna.in", "r") as file:
    lines = [line.strip() for line in file.readlines()]

antenna_map = {}  # char -> (x, y) list
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != ".":
            l = antenna_map.get(char, [])
            l.append((i, j))
            antenna_map[char] = l

rows = len(lines)
cols = len(lines[0])


def inbounds(x, y):
    return 0 <= x < rows and 0 <= y < cols


antinodes = set()
for l in antenna_map.values():
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            x1, y1 = l[i]
            x2, y2 = l[j]
            dx, dy = x2 - x1, y2 - y1
            if inbounds(x2 + dx, y2 + dy):
                antinodes.add((x2 + dx, y2 + dy))
            if inbounds(x1 - dx, y1 - dy):
                antinodes.add((x1 - dx, y1 - dy))
            if x1 % 3 == x2 % 3 and y1 % 3 == y2 % 3:
                if inbounds((x1 * 2 + x2) // 3, (y1 * 2 + y2) // 3):
                    antinodes.add((x1 * 2 + x2) // 3, (y1 * 2 + y2) // 3)
                if inbounds((x1 + x2 * 2) // 3, (y1 + y2 * 2) // 3):
                    antinodes.add((x1 + x2 * 2) // 3, (y1 + y2 * 2) // 3)

print(len(antinodes))
