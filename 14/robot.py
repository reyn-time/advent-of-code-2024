# Read the input file
from functools import reduce


with open("14/robot.in", "r") as file:
    lines = file.readlines()

time = 100
W = 101
H = 103

quadrants = [0, 0, 0, 0]

# Parse the input file
for line in lines:
    ps, vs = line.strip().split(" ")
    x, y = tuple(map(int, ps.split("=")[1].split(",")))
    vx, vy = tuple(map(int, vs.split("=")[1].split(",")))
    final_x, final_y = (x + vx * time) % W, (y + vy * time) % H
    if final_x < W // 2 and final_y < H // 2:
        quadrants[0] += 1
    elif final_x < W // 2 and final_y > H // 2:
        quadrants[1] += 1
    elif final_x > W // 2 and final_y < H // 2:
        quadrants[2] += 1
    elif final_x > W // 2 and final_y > H // 2:
        quadrants[3] += 1

print(reduce(lambda x, y: x * y, quadrants))
