with open('day14.txt', 'r') as file:
    f = [x.strip() for x in file.readlines()]

def maskbit(ma,sk):
    if ma == '0':
        return sk
    return ma

def enum(mas):
    sta = [mas]
    for i in range(pow(2,mas.count('X'))-1):
        pops = sta[0]
        i = pops.find('X')
        sta = sta[1:]+[
            pops[:i]+'0'+pops[i+1:],
            pops[:i]+'1'+pops[i+1:]
        ]
    return sta

def mask(mas,num):
    s = format(num,'b').zfill(len(mas))
    return "".join([maskbit(mas[i],s[i]) for i in range(len(mas))])

from collections import defaultdict
mem = defaultdict(int)

for ro in f:
    if ro[:2] == 'ma':
        mas = ro.split()[2]
    if ro[:2] == 'me':
        num = int(ro.split()[2])
        mem0 = int(ro.split()[0][4:][:-1])
        print(format(mem0,'b'), mas, mask(mas,mem0))
        print(len(enum(mask(mas,mem0))), enum(mask(mas,mem0))[0], enum(mask(mas,mem0))[-1])
        for m in enum(mask(mas,mem0)):
            mem[int(m,2)] = num

print("part2 : ", sum(mem.values()))
