from math import ceil

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


with open("14/robot.in", "r") as file:
    lines = file.readlines()

time = 100
W = 101
H = 103

# Parse the input file
robots = []
for line in lines:
    ps, vs = line.strip().split(" ")
    x, y = tuple(map(int, ps.split("=")[1].split(",")))
    vx, vy = tuple(map(int, vs.split("=")[1].split(",")))
    robots.append((x, y, vx, vy))


edge_partition = 3
bin_count = edge_partition**2


def compute_variance(time):
    bins = [0] * bin_count
    for x, y, vx, vy in robots:
        final_x, final_y = (x + vx * time) % W, (y + vy * time) % H
        x_cut = final_x // ceil(W / edge_partition)
        y_cut = final_y // ceil(H / edge_partition)
        bin_index = x_cut * edge_partition + y_cut
        bins[bin_index] += 1

    variance = 0
    for bin in bins:
        variance += (bin - len(robots) / bin_count) ** 2
    return variance


# Animation
def init():
    plt.xlim(0, W)
    plt.ylim(0, H)
    return (sc, text)


def animate(time):
    xs = []
    ys = []
    for x, y, vx, vy in robots:
        xs.append((x + vx * time) % W)
        ys.append(-(y + vy * time) % H)
    sc.set_offsets(list(zip(xs, ys)))
    text.set_text(f"Time: {time}")


fig, ax = plt.subplots()
sc = ax.scatter([], [])
text = ax.text(0.05, 0.95, "", transform=ax.transAxes)

# Find high variance time frames, i.e. when the robots are concentrated at some columns
variances = [
    (time, compute_variance(time))
    for time in range(W * H)
    if compute_variance(time) > 10000
]

animation = FuncAnimation(
    fig,
    animate,
    frames=[time for time, _ in reversed(variances)],
    interval=500,
    init_func=init,
)
plt.show()
