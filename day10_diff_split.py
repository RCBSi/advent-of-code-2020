import numpy
with open('day10.txt', 'r') as file:
    t = [int(x.strip()) for x in file.readlines()]

def shrink(bit):
    if bit == '':
        return 1
    if bit == '1':
        return 1
    if bit == '11':
        return 2
    if bit == '111':
        return 4
    if bit == '1111':
        return 7
    print("cannot evaluate bit ", bit)

t.append(0)
t.append(max(t)+3)
t.sort()
td = [t[i+1] - t[i] for i in range(len(t)-1)]
print("part 1: ", td.count(1) * td.count(3))
tds = ''.join([str(x) for x in td])
bits = tds.split('3')
print("part 2: ", numpy.prod([shrink(bit) for bit in bits]))
