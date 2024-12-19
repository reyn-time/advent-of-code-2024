program = [2, 4, 1, 1, 7, 5, 1, 5, 4, 0, 5, 5, 0, 3, 3, 0]
a = 64854237
b = 0
c = 0


def combo(v):
    if v <= 3:
        return v
    elif v == 4:
        return a
    elif v == 5:
        return b
    elif v == 6:
        return c


output = []
ptr = 0
while ptr + 1 < len(program):
    print(ptr)
    match program[ptr]:
        case 0:
            a = a // (2 ** combo(program[ptr + 1]))
            ptr += 2
        case 1:
            b = b ^ program[ptr + 1]
            ptr += 2
        case 2:
            b = combo(program[ptr + 1]) % 8
            ptr += 2
        case 3:
            if a == 0:
                ptr += 2
            else:
                ptr = program[ptr + 1]
        case 4:
            b = b ^ c
            ptr += 2
        case 5:
            output.append(combo(program[ptr + 1]) % 8)
            ptr += 2
        case 6:
            b = a // (2 ** combo(program[ptr + 1]))
            ptr += 2
        case 7:
            c = a // (2 ** combo(program[ptr + 1]))
            ptr += 2

print(",".join(map(str, output)))
