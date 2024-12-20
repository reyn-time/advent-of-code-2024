# Read the input
with open("19/towel.in", "r") as file:
    towels = file.readline().strip().split(", ")
    file.readline()
    targets = [line.strip() for line in file.readlines()]


def can_make(target):
    dp = [False] * len(target)
    for i in range(len(target)):
        for towel in towels:
            if len(towel) > i + 1:
                continue
            if target[i - len(towel) + 1 : i + 1] == towel and (
                len(towel) == i + 1 or dp[i - len(towel)]
            ):
                dp[i] = True
                break

    return dp[-1]


count = 0
for target in targets:
    if can_make(target):
        count += 1

print(count)
