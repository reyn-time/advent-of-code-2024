# Read the input
with open("05/queue.in", "r") as f:
    lines = f.readlines()

is_graph_input = True

# Parse the input
graph = {}
pages = []
for line in lines:
    input = line.strip()

    is_graph_input = "|" in input
    if is_graph_input:
        source, target = input.split("|")
        graph[source] = graph.get(source, []) + [target]
    elif input != "":
        pages.append(input.split(","))

total = 0
for page in pages:
    prior_nodes = set()
    violation = False
    for item in page:
        for target in graph.get(item, []):
            if target in prior_nodes:
                violation = True
                break
        if violation:
            break
        prior_nodes.add(item)

    if not violation:
        total += int(page[(len(page) - 1) // 2])


print(total)
