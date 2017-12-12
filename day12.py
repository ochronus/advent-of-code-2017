import networkx
from networkx.drawing.nx_pydot import write_dot


with open('day12-input.txt') as f:
    lines = f.readlines()

    graph = networkx.Graph()

    for line in lines:
        line = str.replace(line, ' ', '')
        node, neighbours = line.strip().split('<->')
        for neighbour in neighbours.split(','):
            graph.add_edge(node, neighbour)

    write_dot(graph, 'day12-graph.dot')
    print(len(networkx.node_connected_component(graph, '0')))
    print(networkx.number_connected_components(graph))
