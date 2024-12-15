# Read the input file
with open("07/bridge.in", "r") as file:
    lines = [
        (
            int(line.strip().split(":")[0]),
            [int(x) for x in line.strip().split(":")[1].strip().split(" ")],
        )
        for line in file.readlines()
    ]


def exhaust(target, numbers, i, curr):
    if i == len(numbers):
        return target == curr

    return (
        exhaust(target, numbers, i + 1, curr + numbers[i])
        or exhaust(target, numbers, i + 1, curr * numbers[i])
        or exhaust(target, numbers, i + 1, int(str(curr) + str(numbers[i])))
    )


total = 0
for target, numbers in lines:
    if exhaust(target, numbers[1:], 0, numbers[0]):
        total += target

print(total)
