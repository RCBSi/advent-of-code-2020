'''
I found the location of each tile in a 12-by-12 grid by computing the graph-theoretic distance of the tile from each corner. If the distance from corner 0,0 is n and the distance from corner 0,1 is m, then the distance from the top row is (m+n-c)/2 for some constant c. Knowing that tiles x and y share an edge e and knowing the locations of x and y, then the location of edge e can be written as the average, (loc(x) + loc(y))/2 . Multiplying all the locations by 8 should leave 8 empty spaces between each pair of edges..
 
We can locate each # in the final 8*12 grid as follows:
from the location of each # in the tile, we compute the distance to each edge. 
Given the distances from the edges in the final 8*12 grid, we assign to this # a location in the final grid.
 
I.e., I think one can avoid all the group theory (flipping, rotating) completely, and just compute location from "distance to fixed points". 

Pseudocode:
'''

infile = 'day20.txt'
with open(infile, 'r') as file:
    f = [x.strip() for x in file.readlines()]

def is_tile_id(x):
    if x:
        if x[0] == 'T':
            return 1
    return 0

def read_tiles(f,ti,edgelength):
    for i in range(len(f)):
        if is_tile_id(f[i]):
            ti[int(f[i][5:-1])] = [f[i+j] for j in range(1,edgelength+1)]
    return ti

def read_edges_from_tile(input_tile, edgelength):
    return [x for x in distance_to_edges(0,0,input_tile, edgelength).keys()]

def distance_to_edges(di,dj, input_tile,edgelength):
    de = {}
    de[''.join(input_tile[0])] = di
    de[''.join([x[edgelength-1] for x in input_tile])] = edgelength - dj - 1
    de[''.join(input_tile[-1][::-1])] = edgelength - di - 1
    de[''.join([x[0] for x in input_tile][::-1])] = dj
    return de

def edge_dist_to_val(input_tile,edgelength,edgelist):
    lookup = {}
    for m in range(edgelength):
        for n in range(edgelength-2):
            for ed in edgelist[]:
                lookup[[distance_to_edges(m,n)[ed] for ed in edgelist]] = input_tile[m][n]
    return lookup

from collections import defaultdict

def edt(ed): # edge-to-tiles function, from tile_to_edge_function 'ed'.
    et = defaultdict(set)
    for te in [[t,e] for t in ed for e in ed[t]]:
        key = min([te[1],te[1][::-1]])
        et[key].add(te[0])
    return et

def gr(et): # find the neighbors of each tile, given the graph on tiles.
    graph = [et[x] for x in et if len(et[x]) > 1]
    ne = defaultdict(set)
    [ne[y].add(z) for x in graph for y in x for z in x if y != z]
    return ne

def cd(ne,el): #create a distance function from an element to the rest of the graph.
    di = {el:0}
    ct = 0
    while len(di) < len(ne) and len(di) > ct:
        ct = len(di)
        di = di | {x:di[y]+1 for y in di for x in ne[y] if not(x in di)}
    return di

def invert_distance_to_tiles(d0,d1):
    out = {}
    for t in d0:
        out = out | {(d0[t],d1[t]): t}
    return out

def which_edge_matches(et,d0,d1):
    out = {}
    for edge in et:
        if len(et[edge]) == 2:
            locs = [[d0[t], d1[t]] for t in et[edge]]
            locs.sort()
            x = 0.5*(locs[0][0] + locs[1][0])
            y = 0.5*(locs[0][1] + locs[1][1])
            out= out|{(x,y):edge}
    return out

with open('day20.txt', 'r') as file:
    f = [x.strip() for x in file.readlines()]

edgelength = len(f[1])
t = read_tiles(f,{},edgelength)
ed = {k:read_edges_from_tile(t[k],edgelength) for k in t}
et = edt(ed)
ne = gr(et)
oc = [x for x in ne if len(ne[x])==2] # obligate corners
d00 = cd(ne,oc[0])
opposite = [x for x in d00 if d00[x]== max(d00.values())][0]
oc1 = [x for x in oc if x != oc[0] and x != opposite]
d01 = cd(ne, oc1[0])
d10 = cd(ne, oc1[1])
d1 = {x:(d00[x] + d01[x]-d00[oc1[0]])//2 for x in d00}
d0 = {x:(d00[x] + d10[x]-d00[oc1[0]])//2 for x in d00}
pm = invert_distance_to_tiles(d0,d1)
we = which_edge_matches(et,d0,d1)
final_size = (edgelength - 2) * (max(d0.values()) + 1)
mat = [['' for x in range(final_size)] for x in range(final_size)]
((i,j),(di,dj)) = ((4,5),(1,3))

for i in range((max(d0.values()) + 1)), j likewise:
    lookup = edge_dist_to_val(t[pm[(i,j)]],edgelength,edgelist)
    for di in (range(edgelength-2) , dj likewise:
        mat[i*(edgelength - 2)+di][j*(edgelength - 2)+dj]=
        lookup[
        distance di from we[(i-0.5,j)] if that exists,
        distance dj from we[(i,j-0.5)] if that exists,
        distance 8-di from we[(i+0.5,j)] if that exists,
        distance 8-dj from we[(i,j+0.5)] if that exists ]
        # find that m,n such that tile element (m,n) has distance di to we[(i-0.5,j)] if that exists,


breakpoint()

'''
The pseudocode has a problem that edges can flip. Solution: decide right at the beginning to always report an edge as the min of itself and its flipped value.

From each tile, create a dictionary: 
D = the color of the node which is in tile T, and which has distance d0 to edge e0, d1 to edge e1, d2 to edge e2, d3 to e3, is '#'. 
That's four edges, four distances.
wheen we want to color (i*8 + di, j*8 + dj), we note that this place has distance di from we[(i,j)(i-1,j)], distance 8-di from we[(i,j)(i+1,j)], 
distance dj from we[(i,j)(i,j-1)] and distance 8-dj from we[(i,j)(i,j+1)]. Of these, some may not exist, i.e., if i-1 < 0 or i+1=8. 
We want to look up the color of the element in tile ti which has these distances. 
One solution would be to create D after pm has been created, and throw away the edges that are at the endge of the final matrix. 
Or we could define D to accept any number 2-4 of edges :-) 4-choose-2 = 6; D will be 6-times bigger, but now the color of (di,dj) is a *lookup* and not a search.




'''
