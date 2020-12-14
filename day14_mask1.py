with open('day14.txt', 'r') as file:
    f = [x.strip() for x in file.readlines()]

def maskbit(ma,sk):
    if ma == 'X':
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
    return int("".join([maskbit(mas[i],s[i]) for i in range(len(mas))]),2)

from collections import defaultdict
mem = defaultdict(int)

mas = f[0].split()[2]
num = int(f[1].split()[2])

for ro in f:
    if ro[:2] == 'ma':
        mas = ro.split()[2]
    if ro[:2] == 'me':
        num = int(ro.split()[2])
        print(mas, num, mask(mas, num))
        mem[ro.split()[0][4:][:-1]] = mask(mas,num)

print("part1 : ", sum(mem.values()))
