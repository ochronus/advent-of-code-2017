import networkx
from networkx.drawing.nx_pydot import write_dot


def build_graph(lines):
    graph = networkx.DiGraph()
    for line in lines:
        node_name = line.split()[0]
        node_weight = int(line.split()[1].strip('()'))
        graph.add_node(node_name, weight=node_weight)
        line_parts = line.split('->')
        if len(line_parts) > 1:
            children = [n.strip() for n in line_parts[1].split(',')]
            for kiddo in children:
                graph.add_edge(node_name, kiddo)

    return graph


def part1(graph):
    return list(networkx.topological_sort(graph))[0]


def part2(graph):
    reversed_graph = reversed(list(networkx.topological_sort(graph)))
    node_weights = {}

    for node in reversed_graph:
        total = graph.nodes[node]['weight']
        child_weight = None
        unbalanced_node = None

        for child in graph[node]:
            if  node_weights[child] != child_weight and child_weight is not None:
                # we'be found a child node with a different weight than the others, this must be it
                unbalanced_node = child
                break

            child_weight = node_weights[child]       # so we can compare with the next child's weight
            total += node_weights[child]

        if unbalanced_node:
            weight_adjustment = abs(child_weight - node_weights[unbalanced_node])         # the node weight should be adjusted by this amount
            return (graph.nodes[unbalanced_node]['weight'] - weight_adjustment)

        node_weights[node] = total          # which is the sum of its children's weight


with open('day7-input.txt') as f:
    lines = [line.rstrip() for line in f]
    graph = build_graph(lines)
    write_dot(graph, 'graph.dot')

    print(part1(graph))
    print(part2(graph))

