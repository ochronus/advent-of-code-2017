# http://adventofcode.com/2017/day/3
# hint: https://oeis.org/A141481


def check_bounce_needed(horizontal_pos, vertical_pos):
    return (horizontal_pos == vertical_pos) \
           or (horizontal_pos < 0 and horizontal_pos == -vertical_pos) \
           or (horizontal_pos > 0 and horizontal_pos == 1 - vertical_pos)

# part 1 is simple math though, bottom right corners are odd square numbers
# here's a brute force solution, just for the sake of coding
def part1(goal):
    horizontal_pos = 0
    vertical_pos = 0
    horizontal_delta = 0
    vertical_delta = -1
    step = 0

    while True:
        step += 1
        if goal == step:
            return (abs(horizontal_pos) + abs(vertical_pos))

        if check_bounce_needed(horizontal_pos, vertical_pos):
            horizontal_delta, vertical_delta = -vertical_delta, horizontal_delta

        # step
        horizontal_pos, vertical_pos = horizontal_pos+horizontal_delta, vertical_pos+vertical_delta


def part2(goal):
    horizontal_pos = 0
    vertical_pos = 0
    horizontal_delta = 0
    vertical_delta = -1
    spiral = {}
    nav_coords = [(1, 0), (1, -1),
                  (0, -1), (-1, -1),
                  (-1, 0), (-1, 1),
                  (0, 1), (1, 1)]

    while True:
        sum = 0
        for offset in nav_coords:
            horizontal_offset, vertical_offset = offset
            if (horizontal_pos + horizontal_offset, vertical_pos + vertical_offset) in spiral:
                sum += spiral[(horizontal_pos + horizontal_offset, vertical_pos + vertical_offset)]

        if sum > goal:
            return sum

        if (horizontal_pos, vertical_pos) == (0, 0):        # center of the spiral
            spiral[(0, 0)] = 1
        else:
            spiral[(horizontal_pos, vertical_pos)] = sum

        if check_bounce_needed(horizontal_pos, vertical_pos):
            horizontal_delta, vertical_delta = -vertical_delta, horizontal_delta

        # step
        horizontal_pos, vertical_pos = horizontal_pos+horizontal_delta, vertical_pos+vertical_delta


input = 312051

print(part1(input))
print(part2(input))
