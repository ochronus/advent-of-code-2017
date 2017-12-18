from collections import defaultdict
from multiprocessing import Queue
from multiprocessing.pool import ThreadPool


def val_or_reg(arg, regs):                # command arguments are either numbers or register names
    try:
        return int(arg)
    except ValueError:
        return regs[arg]


def perform(program_id, instructions, in_queue, out_queue):
    regs = defaultdict(int)
    regs['p'] = program_id


    instruction_counter = 0
    sent_counter = 0                # for part 2
    played_freq = 0
    max_instruction_index = len(instructions) - 1

    while instruction_counter < max_instruction_index:
        try:
            cmd, arg1, arg2 = instructions[instruction_counter].split()
        except ValueError:              # one parameter instruction (rcv or snd)
            cmd, arg1  = instructions[instruction_counter].split()

        if cmd == 'set': regs[arg1] = val_or_reg(arg2, regs)
        if cmd == 'add': regs[arg1] += val_or_reg(arg2, regs)
        if cmd == 'mul': regs[arg1] *= val_or_reg(arg2, regs)
        if cmd == 'mod': regs[arg1] %= val_or_reg(arg2, regs)

        if cmd == 'snd':
            played_freq = val_or_reg(arg1, regs)
            if out_queue:
                out_queue.put(played_freq)
                sent_counter += 1

        if cmd == 'rcv':
            if in_queue:
                regs[arg1] = in_queue.get()
            elif regs[arg1] != 0:
                return played_freq

        if cmd == 'jgz':
            if val_or_reg(arg1, regs) > 0:
                instruction_counter += val_or_reg(arg2, regs)
                continue

        instruction_counter += 1

    return sent_counter


with open('day18-input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    print(perform(0, lines, None, None))

    duet = ThreadPool(processes=2)
    queue1 = Queue()
    queue2 = Queue()
    result1 = duet.apply_async(perform, (0, lines, queue1, queue2))
    result2 = duet.apply_async(perform, (1, lines, queue2, queue1))         # one program's input queue is the other's output queue and vica versa

    result1.get()               # wait for completion
    print(result2.get())