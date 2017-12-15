from operator import xor
from functools import reduce
import numpy as np
from networkx import nx

def twist(state, lengths, n=256, iterations=64):
    skip_size = 0
    current_position = 0
    for i in range(iterations):
        for length in lengths:
            for i in range(length//2):
                i1 = (current_position + i) % n
                i2 = (current_position + length - i - 1) % n
                state[i1], state[i2] = state[i2], state[i1]
            current_position += length + skip_size
            skip_size += 1

def knot_hash(data, n=256):
    state = list(range(n))
    lengths = [ord(x) for x in data] + [17, 31, 73, 47, 23]
    twist(state, lengths, n)
    reduced = [reduce(xor, state[16*i:16*(i+1)]) for i in range(16)]
    return bytes(reduced).hex()


def to_matrix(key):
    s = ''.join(format(int(knot_hash(f'{key}-{i}'), 16), '0128b') for i in range(128))
    return(np.fromiter(s, dtype=int).reshape(128, 128))

def part1(matrix):
    return(matrix.sum())

key = 'ljoxqyyw'
matrix = to_matrix(key)
print(part1(matrix))

graph = nx.Graph()
for row in range(128):
    for col in range(128):
        if matrix[row][col]:
            graph.add_node((row, col))

for row in range(128):
    for col in range(128):
        if row > 0:
            if matrix[row][col] and matrix[row-1][col]:
                graph.add_edge((row, col), (row-1, col))
        if col > 0:
            if matrix[row][col] and matrix[row][col-1]:
                graph.add_edge((row, col), (row, col-1))

print(len(list(nx.connected_components(graph))))