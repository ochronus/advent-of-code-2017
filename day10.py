input = open("day10-input.txt").read().strip()

lengths_part1 = [int(x) for x in input.split(",")]
lengths_part2 = [ord(x) for x in input] + [17, 31, 73, 47, 23]


def twist(seq, start, twist_length):
    # since the list is circular, simple python list slicing won't work
    # we'll instead simply swap elements. We need to iterate up until floor(half) of the list
    for i in range(twist_length // 2):
        first_elem = (start + i) % len(seq)
        second_elem = (start + twist_length - 1 - i) % len(seq)
        seq[first_elem], seq[second_elem] = seq[second_elem], seq[first_elem]


def run(lengths, rounds):
    position = 0
    skip = 0
    sequence = list(range(256))

    for _ in range(rounds):
        for current_length in lengths:
            twist(sequence, position, current_length)
            position += current_length + skip
            skip += 1

    return sequence


def knot_to_hash(knot_seq):
    hash_string = ""

    for current_block_index in range(len(knot_seq) // 16):                        # we have 16 blocks
        xored_num = 0
        for current_num_index in range(16):
            xored_num ^= knot_seq[current_block_index * 16 + current_num_index]   # iterate inside the current block of 16 numbers
        padded_hex = hex(xored_num)[2:].zfill(2)                                  # convert the current number to its zero-padded hex representation
        hash_string += padded_hex

    return(hash_string)


knot_seq1 = run(lengths_part1, 1)
print(knot_seq1[0] * knot_seq1[1])

knot_seq2 = run(lengths_part2, 64)
print(knot_to_hash(knot_seq2))