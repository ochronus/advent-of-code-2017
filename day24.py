with open('day24-input.txt') as components_file:
    components = [tuple(map(int, s.strip().split('/')))
                  for s in components_file.readlines()]


def get_available_components(last_port, already_in_use):
    return ( (component_index, component) for component_index, component in enumerate(components) if last_port in component and component_index not in already_in_use)


def part1(last_port=0, already_in_use=set()):
    max_strength = 0

    for component_index, component in get_available_components(last_port, already_in_use):
        already_in_use.add(component_index)

        strength = part1(
            component[0] if component[1] == last_port else component[1],
            already_in_use
        )

        if strength + sum(component) > max_strength:
            max_strength = strength + sum(component)

        already_in_use.remove(component_index)

    return max_strength


def part2(last_port=0, already_in_use=set()):
    max_length, max_strength = 0, 0

    for component_index, component in get_available_components(last_port, already_in_use):
        already_in_use.add(component_index)

        length, strength = part2(
            component[0] if component[1] == last_port else component[1],
            already_in_use
        )

        if length + 1 > max_length or (length + 1 == max_length and strength + sum(component) > max_strength):
            max_length = length + 1
            max_strength = strength + sum(component)

        already_in_use.remove(component_index)

    return max_length, max_strength


print(part1())
print(part2()[1])
