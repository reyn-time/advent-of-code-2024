def is_safe(input):
    if len(input) <= 1:
        return True
    increasing = input[1] > input[0]

    for i in range(1, len(input)):
        if increasing and (input[i] <= input[i - 1] or input[i] - input[i - 1] > 3):
            return False
        if not increasing and (input[i] >= input[i - 1] or input[i - 1] - input[i] > 3):
            return False
    return True


# Read input from file
count = 0
with open("02/level.in", "r") as file:
    for line in file:
        input = list(map(int, line.strip().split(" ")))
        if is_safe(input):
            count += 1

print(count)
