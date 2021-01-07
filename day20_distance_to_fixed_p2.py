import numpy
from collections import defaultdict

with open('day20.txt', 'r') as file:
    f = {t[5:9] : numpy.array([[y for y in x] for x in t.strip()[11:].split('\n')]) for t in file.read().split('\n\n') if t}

def soi(x): # self_or_inverse():
    if ''.join(x[::-1]) < ''.join(x):
        return x[::-1]
    return x

def cd(ne,el): #create a distance function from an element to the rest of the graph.
    di, ct = ({el:0},0)
    while len(di) < len(ne) and len(di) > ct:
        ct = len(di)
        di = di | {x:di[y]+1 for y in di for x in ne[y] if not(x in di)}
    return di

et, ne, we = (defaultdict(set), defaultdict(set), defaultdict(set)) # edge-to-tiles, neighbors, a inverse to et, mapping pairs of tiles to the edge between them.
for x in f:
    for y in [soi(f[x][:,-1]), soi(f[x][:, 0]), soi(f[x][0, :]), soi(f[x][-1,:])]:
        for z in et[''.join(y)]:
            ne[z].add(x)
            ne[x].add(z)
        et[''.join(y)].add(x)
        if len(et[''.join(y)]) == 2:
            we[''.join(soi([x for x in et[''.join(y)]]))] = y

oc = [x for x in ne if len(ne[x])==2] # obligate corners
print("part1",numpy.prod([int(x) for x in oc]))
d00 = cd(ne,oc[0])
oc1 = [x for x in oc if x != oc[0] and x != [x for x in d00 if d00[x]== max(d00.values())][0]] # x!= tile opposite from oc[0]
d01, d10 = (cd(ne, oc1[0]), cd(ne, oc1[1]))
d1 = {x:(d00[x] + d01[x]-d00[oc1[0]])//2 for x in d00}
d0 = {x:(d00[x] + d10[x]-d00[oc1[0]])//2 for x in d00}
pm = {(d0[t],d1[t]):t for t in d00} # location to tile. lt = pm "place in the matrix"
r0,r1 = (range((max(d0.values()) + 1)), range(len(f[oc[0]]) - 2))
mat = numpy.array([['' for y in r0 for y1 in r1] for x in r0 for x1 in r1]) # numpy.array(mat)[10][50] == numpy.array(mat)[(10,50)]
tl,tij = ([(x,y) for y in r0 for x in r0], [(x,y) for y in r1 for x in r1])
de = {}
breakpoint()
for ti in [ti for ti in f.values()]+ [numpy.array([[y for y in x] for x in zip(*ti)]) for ti in f.values()]:
#    for ti in [ti0, numpy.array([[y for y in x] for x in zip(*ti0)])] for ti0 in f.values():
    de = de|{''.join(ti[:, 0])+str(1+dj)+''.join(ti[ 0, :])+str(1+di) :ti[(di,dj)] for (di,dj) in tij}
    de = de|{''.join(ti[:,-1])+str(8-dj)+''.join(ti[ 0, :])+str(1+di) :ti[(di,dj)] for (di,dj) in tij}
    de = de|{''.join(ti[:,-1])+str(8-dj)+''.join(ti[-1, :])+str(8-di) :ti[(di,dj)] for (di,dj) in tij}
    de = de|{''.join(ti[:, 0])+str(1+dj)+''.join(ti[-1, :])+str(8-di) :ti[(di,dj)] for (di,dj) in tij}
    
breakpoint()
for i,j in tl: # here, we can restict our search to one vertical and one horizontal edge, but in de we don't know oriendation.
    for (di,dj) in tij:
        if j < 6:
            vertical = ''.join(we[''.join(soi([pm[(i,j)],pm[(i,j+1)]]))])+str(8-dj)
        else:
            vertical = ''.join(we[''.join(soi([pm[(i,j)],pm[(i,j-1)]]))])+str(1+dj)
        if i < 6:
            horizontal = ''.join(we[''.join(soi([pm[(i,j)],pm[(i+1,j)]]))])+str(8-di)
        else:
            horizontal = ''.join(we[''.join(soi([pm[(i,j)],pm[(i-1,j)]]))])+str(1+di)
        mat[(i*(len(f[oc[0]]) - 2)+di,j*(len(f[oc[0]]) - 2)+dj)] = de[vertical+horizontal]

breakpoint()

seas = ['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   '] # Sea Serpent filter.
sealist = [(i,j) for i in range(len(seas)) for j in range(len(seas[0])) if seas[i][j] == '#']
s0 = sum(sum(mat=='#'))
ml = [mat, mat[:,::-1], mat[::-1,::-1], mat[::-1,:]]
mz = [numpy.array([[y for y in x] for x in zip(*x)]) for x in ml]
for mat in ml+mz:
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i + 3 in range(len(mat)):
                if j + 20 in range(len(mat)):
                    if sum([1 for di in range(len(seas)) for dj in range(len(seas[0])) if mat[i+di][j+dj] == '#' and (di, dj) in sealist]) == 15:
                        for (di,dj) in sealist:
                            mat[i+di][j+dj] = 'O'
    if sum(sum(mat=='#')) < s0:
        print('\n'.join(''.join(y) for y in mat))
        print("part 2", sum(sum(mat=='#')))
        break
breakpoint()
