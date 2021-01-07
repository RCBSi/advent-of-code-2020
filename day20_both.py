# deciding the color of (8*i + di, 8*j + dj) based on the distances from di and dj to the edges is tempting, and 
# computing the flip is tempting, but with ony 8 flips, we can easily check them all, as jv does. 
# computing the location of each tile is lets us handle n tiles in O(n), not O(n^2) = "for each tile, search all unused tiles". 
# Even for n about 100, the runtime of O(n^2) is a few seconds. 

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

def fits(ti,tl):
    d1 = {(0,1):soi(ti[:,-1]), (0,-1):soi(ti[:, 0]), (-1,0):soi(ti[0, :]), (1,0):soi(ti[-1,:])}
    for (k,l) in [(di,dj) for (di,dj) in d1 if (i+di,j+dj) in tl]: # check all edges, though it is
        if sum(d1[(k,l)] != we[''.join(soi([pm[(i,j)],pm[(i+k,j+l)]]))]) > 0:
            return 0
    return 1

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
for i,j in tl:
    fl = [f[pm[(i,j)]], f[pm[(i,j)]][:,::-1], f[pm[(i,j)]][::-1,::-1], f[pm[(i,j)]][::-1,:]]
    fz = [numpy.array([[y for y in x] for x in zip(*x)]) for x in fl]
    for ti in fl+fz:
        if fits(ti,tl):
            for (di,dj) in [(x,y) for y in r1 for x in r1]:
                mat[(i*(len(f[oc[0]]) - 2)+di,j*(len(f[oc[0]]) - 2)+dj)] = ti[(di+1,dj+1)]
            break

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
