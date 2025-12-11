import functools
def parse(fp):
    # key: node name, value: names of nodes that can be reached from key
    graph = {}
    for line in open(fp):
        k, v = line.split(": ")
        v = tuple(v.strip().split())
        graph[k] = v
    return graph
def traverse(from_node, to_node, graph):
    result = 0
    for node in graph[from_node]:
        if node == to_node:
            result += 1
        elif node in graph:
            result += traverse(node, to_node, graph)
    return result
def part_1(fp):
    graph = parse(fp)
    return traverse("you", "out", graph)
def part_2(fp):
    graph = parse(fp)

if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))