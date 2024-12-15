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
    in_degree = {item: 0 for item in page}
    for item in page:
        for target in graph.get(item, []):
            if target in in_degree:
                in_degree[target] += 1

    sorted_list = []
    while len(sorted_list) < len(page):
        for item in in_degree:
            if in_degree[item] == 0:
                sorted_list.append(item)
                break
        del in_degree[item]
        for target in graph.get(item, []):
            if target in in_degree:
                in_degree[target] -= 1

    if page != sorted_list:
        total += int(sorted_list[len(sorted_list) // 2])


print(total)
