import re
import math

cmds = [line.split() for line in open('day23-input.txt','r').readlines()]
regs = [0 for _ in range(8)]

def getval(r):
    if re.match('[\-0-9]',r):
        return int(r)
    else:
        return regs[ord(r) - 97]
i1 = 0
m = 0
while 0 <= i1 < len(cmds):
    cmd = cmds[i1]
    c = cmd[0]
    if c == 'jnz':
        if getval(cmd[1]) != 0:
            i1 += getval(cmd[2])
        else:
            i1 += 1
    else:
        if c == 'set':
            regs[ord(cmd[1]) - 97] = getval(cmd[2])
        if c == 'sub':
            regs[ord(cmd[1]) - 97] -= getval(cmd[2])
        if c == 'mul':
            regs[ord(cmd[1]) - 97] *= getval(cmd[2])
            m += 1
        i1 += 1
print(m)
print(regs)                             # [0, 79, 79, 79, 79, 1, 0, 0]
h = 0
range_from = regs[1] * 100 + 100000     # 107900
range_to = range_from + 17000           # 124900

# the code is basically a primality check
for num in range(range_from, range_to + 1, 17):
    for divisor in range(2, math.ceil(math.sqrt(num))):
        if num % divisor == 0:
            h += 1
            break
print(h)