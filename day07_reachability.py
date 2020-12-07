import re
from collections import defaultdict

def cost(x, n):
    if len(n[x]) == 0:
        return 1
    return 1+sum([cost(y[2:], n)*int(y[0]) for y in n[x]])

with open('day07.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]
multi_edges = [re.findall('(\w+\s\w+)\sbag',x,2) for x in t]
arrows = [(x[0], y) for x in multi_edges for y in x if y != x[0]]
neigh = defaultdict(set)
for x, y in arrows:
    neigh[y].add(x)
reachable =neigh['shiny gold']
go_on = 1
while go_on:
    go_on = 0
    for x in reachable:
        go_on += len(neigh[x].difference(reachable))
        reachable = reachable.union(neigh[x])
    print("part 1 >=", len(reachable))

ledges = [re.findall('(.?\s?\w+\s\w+)\sbag',x,2) for x in t]
larrows = [(x[0], y) for x in ledges for y in x if y != x[0] and y[0] != 'n']
lneigh = defaultdict(set)
for x, y in larrows:
    lneigh[x].add(y)

print("part 2", cost('shiny gold',lneigh)-1)
