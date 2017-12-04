input_ = open('day4-input.txt').read().splitlines()

def part1(lines):
    return sum(map(lambda line: int(len(line.split()) == len(set(line.split()))), lines))

def part2(lines):
    return sum(map(lambda line: int(len(line.split()) == len({tuple(sorted(word)) for word in line.split()})), lines))

print(part1(input_))
print(part2(input_))
