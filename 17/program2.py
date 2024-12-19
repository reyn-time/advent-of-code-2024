# The question's code in Python form.
def get_output(a):
    output = []
    while True:
        b = (a & 7) ^ 1  # Last 3 bits of a, and last bit flipped
        c = a >> b  # Essentially a right-shift of a, by b bits (at most 7).
        b = b ^ 5  # Flip bit 1 and 3
        b = b ^ c  # Flip by last 3 bits of c
        output.append(b & 7)
        a >>= 3  # Shift right 3 bits
        if a == 0:
            break
    return output


# Analysis of program above: Each iteration of the loop, b and c are totally determined by the value of a.
# In fact, it is determined by a few bits of a.
output_to_possible_combinations = {}
binary = ["000", "001", "010", "011", "100", "101", "110", "111"]

for shift in range(8):
    a_last_3 = shift ^ 1
    if shift < 3:
        fixed_digits = 3 - shift
        non_fixed_digits = shift
        for i in range(2**non_fixed_digits):
            c = (i << fixed_digits) + (a_last_3 >> non_fixed_digits)
            output = (shift ^ c ^ 5) & 7
            if output not in output_to_possible_combinations:
                output_to_possible_combinations[output] = []
            output_to_possible_combinations[output].append(
                (binary[a_last_3], shift, binary[c])
            )
    else:
        for c in range(8):
            output = (shift ^ c ^ 5) & 7
            if output not in output_to_possible_combinations:
                output_to_possible_combinations[output] = []
            output_to_possible_combinations[output].append(
                (binary[a_last_3], shift, binary[c])
            )

offset = 10
wanted_output_list = [2, 4, 1, 1, 7, 5, 1, 5, 4, 0, 5, 5, 0, 3, 3, 0][::-1]
test_array = ["0"] * (offset + len(wanted_output_list) * 3)
min_val = float("inf")


def dfs(index):
    global min_val
    if index == len(wanted_output_list):
        val = int("".join(test_array), 2)
        min_val = min(min_val, val)
        return
    for a_last_3, shift, c in output_to_possible_combinations[
        wanted_output_list[index]
    ]:
        test_array[index * 3 + offset] = a_last_3[0]
        test_array[index * 3 + offset + 1] = a_last_3[1]
        test_array[index * 3 + offset + 2] = a_last_3[2]
        if (
            test_array[index * 3 + offset - shift] == c[0]
            and test_array[index * 3 + offset - shift + 1] == c[1]
            and test_array[index * 3 + offset - shift + 2] == c[2]
        ):
            dfs(index + 1)


dfs(0)
print(min_val)
