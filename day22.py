from collections import defaultdict


def part1(lines):
    N = len(lines)
    infected_nodes = set()
    for y in range(N):
        for x in range(N):
            if lines[y][x] == '#':
                infected_nodes.add(x - N // 2 + (-y + N // 2) * 1j)

    # complex numbers are perfect for 2d grid navigation
    current = 0 + 0j
    direction = 1j

    count = 0
    for _ in range(10_000):
        if current in infected_nodes:
            direction *= -1j  # rotate right
            infected_nodes.remove(current)
        else:
            direction *= 1j  # rotate left
            infected_nodes.add(current)
            count += 1
        current += direction

    print(count)


def part2(lines):
    N = len(lines)
    # 0 = clean, 1 = weakened, 2 = infected, 3 = flagged
    node_states = defaultdict(lambda: 0)
    for y in range(N):
        for x in range(N):
            if lines[y][x] == '#':
                node_states[x - N // 2 + (-y + N // 2) * 1j] = 2

    current = 0 + 0j
    direction = 1j

    count = 0
    for _ in range(10_000_000):
        state = node_states[current]
        if state == 0: direction *= 1j  # rotate left
        elif state == 1: count += 1 
        elif state == 2: direction *= -1j  # rotate right
        else: direction *= -1  # rotate 180 degrees
        if state == 3: del node_states[current]
        else:
            node_states[current] = (node_states[current] + 1) % 4  # states are between 0..3
        current += direction

    print(count)



lines = open("day22-input.txt").readlines()

part1(lines)
part2(lines)