# Read input from file
with open("04/xmas.in", "r") as file:
    input = file.read().strip()

# Split input into lines
lines = [line.strip() for line in input.split("\n")]

# Print the lines
to_search = []

rows = len(lines)
cols = len(lines[0])

count = 0

for i in range(rows):
    for j in range(cols):
        if lines[i][j] == "A" and i > 0 and i < rows - 1 and j > 0 and j < cols - 1:
            # Check for the cross
            if lines[i - 1][j - 1] + lines[i + 1][j + 1] in ["MS", "SM"] and lines[
                i - 1
            ][j + 1] + lines[i + 1][j - 1] in ["MS", "SM"]:
                count += 1

print(count)
