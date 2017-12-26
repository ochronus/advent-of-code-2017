from collections import defaultdict


def symbol(s):
    return int(s.split()[-1][:-1])

def move(s):
    return -1 if s.split()[-1]=='left.' else 1

def get_state(s):
    return s.split()[-1][:-1]


lines = open('day25-input.txt').readlines()
state = lines[0].split()[-1][:-1]
steps = int(lines[1].split()[-2])
rules = defaultdict(dict)


rule_state = chr(ord('A')-1)
for rule_index_in_file in range(5, len(lines), 10):
    rule_state = chr(ord(rule_state)+1)
    rules[rule_state][0] = (symbol(lines[rule_index_in_file]), move(lines[rule_index_in_file+1]), get_state(lines[rule_index_in_file+2]))
    rules[rule_state][1] = (symbol(lines[rule_index_in_file+4]), move(lines[rule_index_in_file+5]), get_state(lines[rule_index_in_file+6]))
print(state, steps)
print(rules)

tape = defaultdict(int)
position = 0

for _ in range(steps):
    #print state, tape[position]
    new_symbol, new_move, new_state = rules[state][tape[position]]
    tape[position] = new_symbol
    state = new_state
    position += new_move

checksum = 0
for _, v in tape.items():
    if v == 1: checksum += 1

print(checksum)
