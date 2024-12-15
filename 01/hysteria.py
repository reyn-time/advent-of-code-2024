# Read input from file
first_array = []
second_array = []
with open("01/hysteria.in", "r") as file:
    for line in file:
        first, second = map(int, line.strip().split("   "))
        first_array.append(first)
        second_array.append(second)

first_array.sort()
second_array.sort()

total = 0
for i in range(len(first_array)):
    total += abs(first_array[i] - second_array[i])

print(total)
