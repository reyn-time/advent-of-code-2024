# Read input from file
first_array = []
second_dict = {}
with open("01/hysteria.in", "r") as file:
    for line in file:
        first, second = map(int, line.strip().split("   "))
        first_array.append(first)
        second_dict[second] = second_dict.get(second, 0) + 1

total = 0
for elem in first_array:
    total += elem * second_dict.get(elem, 0)

print(total)
