with open('day9-input.txt') as f:
    input_stream = f.readline().strip()

total_score = 0
garbage_score = 0

current_nesting = 0
inside_garbage = False
skip_next = False

for token in input_stream:
    if inside_garbage:
        if skip_next:
            skip_next = False
        else:
            if token == ">":
                inside_garbage = False
            elif token == "!":
                skip_next = True
            else:
                garbage_score += 1

    else:
        if token == "<":
            inside_garbage = True
        if token == "{":
            current_nesting += 1
        if token == "}":
            total_score += current_nesting
            current_nesting -= 1


print(total_score)
print(garbage_score)
