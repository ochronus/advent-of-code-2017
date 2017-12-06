# http://adventofcode.com/2017/day/6


def solve(memory_bank_layout, part2):
    already_seen = []
    cycles = 0

    while str(memory_bank_layout) not in already_seen:
        already_seen.append(str(memory_bank_layout))
        redistribute(memory_bank_layout)
        cycles += 1

    if part2:
        return solve(memory_bank_layout, False)
    else:
        return cycles


def redistribute(memory_bank_layout):
    biggest_bank = max(memory_bank_layout)
    start_index = 0
    # find the first occurence of the biggest bank
    for bank_index, bank_size in enumerate(memory_bank_layout):
        if bank_size == biggest_bank:
            start_index = bank_index
            break

    memory_bank_layout[start_index] = 0
    blocks_to_distribute = biggest_bank
    current_bank_index = start_index

    while blocks_to_distribute > 0:
        current_bank_index += 1
        current_bank_index %= len(memory_bank_layout)       # wrap around
        memory_bank_layout[current_bank_index] += 1
        blocks_to_distribute -= 1



with open('day6-input.txt') as input:
    initial_layout = list(map(int, input.read().strip().split()))
    print(solve(initial_layout, False))                     # part 1
    print(solve(initial_layout, True))                      # part 2
