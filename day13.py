with open('day13-input.txt') as f:
    lines = f.readlines()

layer_count = int(lines[-1].split()[0][:-1]) + 1

scanner_ranges = [0 for _ in range(layer_count)]

for line in lines:
    layer_no, scanner_range = line.strip().split()
    layer_no = int(layer_no[:-1])
    scanner_range = int(scanner_range)
    scanner_ranges[layer_no] = scanner_range


def simulate_packet_ride(layer_count, delay=0, part2=False):
    severity = 0

    for layer_index in range(layer_count):
        scanner_range = scanner_ranges[layer_index]
        # e.h. range == 3; let's simulate the bouncing effect by virtually doubling the range
        #
        #          [ ]
        # [ ]      [ ]
        # [ ]  ==> [ ]  <-- counted twice at turns
        # [ ]      [ ]  <-- counted twice at turns
        #          [ ]
        #          [ ]
        #
        #
        real_mirrored_range = (scanner_range * 2 - 2)       # twice the original range minus the 2 slots we count twice
        wall_loc = (layer_index + delay) % real_mirrored_range
        if wall_loc >= scanner_range:                       # let's bounce
            wall_loc = real_mirrored_range - wall_loc

        if wall_loc == 0:                                   # the packet got detected
            if part2:
                return(False)
            else:
                severity += layer_index * scanner_range
    if part2:
        return True
    else:
        return(severity)


print(simulate_packet_ride(layer_count, 0, False))

delay = 0
while True:
    has_passed_through = simulate_packet_ride(layer_count, delay, True)
    if has_passed_through:
        print(delay)
        break
    delay += 1
