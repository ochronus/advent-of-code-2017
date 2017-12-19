with open('day19-input.txt', 'r') as f:
    routing_diagram = f.read().split('\n')[:-1]


x = routing_diagram[0].index('|')
y = 0

direction = 'D'
current_route_char = routing_diagram[y][x]

letter_sequence = []
step_counter = 0

while current_route_char != ' ':
    step_counter += 1

    if direction == 'D': y += 1
    if direction == 'U': y -= 1
    if direction == 'L': x -= 1
    if direction == 'R': x += 1

    current_route_char = routing_diagram[y][x]

    if current_route_char == '|' or  current_route_char == '-':
        continue

    if current_route_char == '+':
        if direction == 'D' or direction == 'U':
            if routing_diagram[y][x-1] != ' ':
                direction = 'L'
            else:
                direction = 'R'
        else:
            if routing_diagram[y-1][x] != ' ':
                direction = 'U'
            else:
                direction = 'D'

    else:
        letter_sequence.append(current_route_char)

print(''.join(letter_sequence))
print(step_counter)
