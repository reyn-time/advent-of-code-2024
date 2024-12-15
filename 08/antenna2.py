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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


antinodes = set()
for l in antenna_map.values():
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            x1, y1 = l[i]
            x2, y2 = l[j]
            dx, dy = x2 - x1, y2 - y1
            g = gcd(abs(dx), abs(dy))
            dx, dy = dx // g, dy // g
            t = 0
            while inbounds(x1 + t * dx, y1 + t * dy):
                antinodes.add((x1 + t * dx, y1 + t * dy))
                t += 1
            t = -1
            while inbounds(x1 + t * dx, y1 + t * dy):
                antinodes.add((x1 + t * dx, y1 + t * dy))
                t -= 1

print(len(antinodes))
