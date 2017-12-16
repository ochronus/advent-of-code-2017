program_list = list("abcdefghijklmnop")
dance_moves = open('day16-input.txt').read().strip().split(',')


def do_a_move(prog_list, dance_move):
    progs = list(prog_list)
    move = dance_move[0]
    if move == 's':                                         # spin
        i = int(dance_move[1:])
        progs = progs[-i:] + progs[:-i]                     # l = ('a', 'b', 'c', 'd') ; l[:-2] == ('a', 'b') ; l[-2:] == , ('c', 'd')
    if move == 'x':                                         # exchange
        prog_1, prog_2 = map(int, dance_move[1:].split('/'))
        progs[prog_1], progs[prog_2] = progs[prog_2], progs[prog_1]
    if move == 'p':                                         # partner
        prog_1, prog_2 = dance_move[1:].split('/')
        prog_1_index = progs.index(prog_1)
        prog_2_index = progs.index(prog_2)
        progs[prog_1_index], progs[prog_2_index] = progs[prog_2_index], progs[prog_1_index]
    
    return progs


def perform_coreography(iterations, programs):
    progs = list(programs)                                  # make a copy as lists are passed by reference
    seen = []
    for i in range(iterations):
        s = ''.join(progs)
        if s in seen:                                       # if we've already seen this configuration, it's a cycle
            print(i, seen[iterations % i])                  # and the solution is total repetitions MOD cycle (no change afer N cycles)
            return
        seen.append(s)
        
        for dance_move in dance_moves:
            progs = do_a_move(progs, dance_move)

    print(''.join(progs))


perform_coreography(1, program_list)
perform_coreography(1000000000, program_list)