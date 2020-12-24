'''
This jigsaw program solves day 20a. 
To solve day 20 part 2, it seems we must actually put together the jigsaw. 
I suggest we create an adjacency graph. 
Then compute the graph-distance (Manhattan distance) of each tile from each corner.
The distance of the corners from each other indicates which corners are adjacent.
Each tile's location in the puzzle can be read from its distance from the corners.
'''

import numpy
with open('day20.txt', 'r') as file:
    f = [x.strip() for x in file.readlines()]

def read_0_edges(f,ed): #top
    for i in range(len(f)):
        if is_tile_id(f[i]):
            ed[int(f[i][5:-1])].append(f[i+1])

def read_1_edges(f,ed,edgelength):
    for i in range(len(f)):
        if is_tile_id(f[i]):
             right_edge = ''.join([f[i+j][edgelength-1] for j in range(1,edgelength+1)])
             ed[int(f[i][5:-1])].append(right_edge)

def read_2_edges(f,ed,edgelength):
    for i in range(len(f)):
        if is_tile_id(f[i]):
            ed[int(f[i][5:-1])].append(f[i+edgelength][::-1])

def read_3_edges(f,ed,edgelength):
    for i in range(len(f)):
        if is_tile_id(f[i]):
             left_edge = ''.join([f[i+j][0] for j in range(1,edgelength+1)])[::-1]
             ed[int(f[i][5:-1])].append(left_edge)

def is_tile_id(x):
    if x:
        if x[0] == 'T':
            return 1
    return 0

def count_matched_edges_per_tile(ed):
    matches_per_tile = {x:0 for x in ed}
    for x in ed:
        erl = [y[::-1] for xx in ed for y in ed[xx] if xx != x]
        elr = [y       for xx in ed for y in ed[xx] if xx != x]
        matches = 0 #_not_flipped = 0
#        matches_flipped = 0
        for y in ed[x]:
            if y in erl or y in elr:
                matches += 1
#            if y in elr:
#                matches_flipped += 1
#        matches_per_tile[x] = max(matches_not_flipped, matches_flipped)
        matches_per_tile[x] = matches
    return matches_per_tile


ed = {int(x[5:-1]):[] for x in f if is_tile_id(x)}
read_0_edges(f,ed)
edgelength = len(ed[2311][0])
read_1_edges(f,ed,edgelength)
read_2_edges(f,ed,edgelength)
read_3_edges(f,ed,edgelength)
ma = count_matched_edges_per_tile(ed)
oc = [x for x in ma if ma[x] == 2] # Obligate corners.
print("Part 1", numpy.prod(oc), "if 4 = ", len(oc))
breakpoint()

'''
[int(x[5:-1]) for x in f if is_tile_id(x)]

[y for x in ed for y in ed[x]]

len(numpy.unique([y for x in ed for y in ed[x]]))

elr = [y for x in ed for y in ed[x]] # all edges, left to right.
erl = [y[::-1] for x in ed for y in ed[x]] # all edges, right to left.

Right-to-left is nonsnse... you are also allowed to flip tiles.
'''
