import re
import numpy
with open('day16.txt', 'r') as file:
    fi = [x.strip() for x in file.readlines()]

def ready(s, used_up):
    if len(s) != 1:
        return 0
    e = next(iter(s))
    if e in used_up:
        return 0
    return 1

def pick(s):
    e = next(iter(s))
    return e

def num_breaks_class(i,x): # x is the class.
    if (i >= x[1] and i <= x[2]) or (i >= x[3] and i <= x[4]):
        return 0
    return 1

def ever_valid(i,classes):
    for x in classes:
        if (i >= x[1] and i <= x[2]) or (i >= x[3] and i <= x[4]):
            return 1
    return 0

def invalid(y, global_min, global_max): # y is the ticket.
    return [int(x) for x in y.split(',') if int(x) < global_min or int(x) > global_max]

classes = []
for i in range(fi.index('')):
    classes.append([i]+ [int(x) for x in re.findall('[0-9]+',fi[i])])

global_max = max([x[4] for x in classes])
global_min = min([x[1] for x in classes])
ev = [i for i in range(global_min, global_max+1) if ever_valid(i, classes)]
#[i for i in range(global_min, global_max+1)] == ev
#TRUE
#nv = [i for i in range(global_min, global_max+1) if not ever_valid(i, classes)]

tickets = [fi[fi.index('')+2]]+fi[fi.index('')+5:]
vt = [y for y in tickets if invalid(y, global_min, global_max) == []]

print("part 1: ",sum([sum(invalid(y, global_min, global_max)) for y in tickets]))

from collections import defaultdict
cf = defaultdict(set)

for field in range(len(vt[0].split(','))):
    values = [int(y.split(',')[field]) for y in vt]
    for cla in classes:
        faults = [num_breaks_class(int(n),cla) for n in values]
        if sum(faults) == 0:
            cf[cla[0]].add(field)

used_up = []
force = [x for x in cf if ready(cf[x], used_up)]

while force:
    for x in force:
        used = next(iter(cf[x]))
        used_up.append(used)
        for a in cf:
            if used in cf[a] and a != x:
                cf[a].remove(used)
    force = [x for x in cf if ready(cf[x], used_up)]

answ = [i for i in range(fi.index('')) if fi[i][:9] == 'departure']

answer_fields = [pick(cf[a]) for a in answ]

multiplicands = [int(tickets[0].split(',')[i]) for i in answer_fields]
print("part 2: ",numpy.prod(multiplicands))
breakpoint()

# NB: answ = [0,1,2,3,4,5]
