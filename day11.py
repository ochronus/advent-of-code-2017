# https://www.redblobgames.com/grids/hexagons/ for inspiration

with open('day11-input.txt') as f:
    child_path = f.readline().strip().split(',')

    # cube coordinates
    x = 0
    y = 0
    z = 0

    max_distance = 0

    for step in child_path:
        if step == 's':
            y -= 1
            z += 1

        if step == 'se':
            x += 1
            y -= 1

        if step == 'sw':
            x -= 1
            z += 1

        if step == 'n':
            y += 1
            z -= 1

        if step == 'ne':
            x += 1
            z -= 1

        if step == 'nw':
            x -= 1
            y += 1

        distance = int((abs(x) + abs(y) + abs(z)) / 2)
        if distance > max_distance :
            max_distance = distance

    print(int((abs(x) + abs(y) + abs(z)) / 2))
    print(max_distance)