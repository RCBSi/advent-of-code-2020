with open('day08.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

def run_to(accumulator, index, t):
    seen = []
    while index not in seen:
        seen.append(index)
        oper =  t[index].split()[0]
        argu =  int(t[index].split()[1])
        if oper == 'nop':
            index += 1
        if oper == 'acc':
            accumulator += argu
            index += 1
        if oper == 'jmp':
            index += argu
    return accumulator

def does_it_halt(accumulator, index, t):
    seen = []
    while index not in seen:
        seen.append(index)
        oper =  t[index].split()[0]
        argu =  int(t[index].split()[1])
        if oper == 'nop':
            index += 1
        if oper == 'acc':
            accumulator += argu
            index += 1
        if oper == 'jmp':
            index += argu
        if index >= len(t):
            return accumulator
    return -99999999

def alt(operargu):
    oper = operargu.split()[0]
    argu = operargu.split()[1]
    if oper == 'nop':
        return 'jmp'+' '+argu
    if oper == 'jmp':
        return 'nop'+' '+argu
    return operargu

print("part 1: ", run_to(0,0,t))
print("part 2: ", max([does_it_halt(0,0,t[:i]+[alt(t[i])]+ t[i+1:]) for i in range(len(t))]))
