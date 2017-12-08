from collections import defaultdict


code_lines = open("day8-input.txt").read().strip().splitlines()

registers = defaultdict(int)
max_value_in_any_reg = 0

for code_line in code_lines:
    reg_to_mod, op, value, _, reg_to_check, comp_op, val_to_compare_with = code_line.strip().split()

    if eval("registers[reg_to_check]" + comp_op + val_to_compare_with):
        if op == 'inc':
            registers[reg_to_mod] += int(value)
        else:
            registers[reg_to_mod] -= int(value)

        max_value_in_any_reg = max(registers[reg_to_mod], max_value_in_any_reg)


print(max(registers.values()))
print(max_value_in_any_reg)