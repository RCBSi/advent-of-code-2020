with open('day06.txt', 'r') as file:
    f = file.read().split('\n\n')

print("part 1 ", sum([len(set(x.replace('\n',''))) for x in f]))
gr = [[set(x) for x in g.strip().split('\n')] for g in f]
print("part 2 ", sum([len(g[0].intersection(*g)) for g in gr]))
