# http://adventofcode.com/2017/day/5

def solve(instructions, part):
    jump = 0
    steps_taken = 0
    local_copy_instructions = list(instructions)
    instruction_count = len(local_copy_instructions)

    while jump < instruction_count and jump >= 0:
        j = local_copy_instructions[jump]
        if j >= 3 and part == 1:
            local_copy_instructions[jump] -= 1
        else:
            local_copy_instructions[jump] += 1
        jump += j
        steps_taken += 1

    return steps_taken

instructions = list(map(int,[x.rstrip() for x in open('day5-input.txt','r').readlines()]))

print(solve(instructions, 0))
print(solve(instructions, 1))
