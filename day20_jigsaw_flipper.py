import numpy

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

def read_tiles(f,ti,edgelength):
    ti ={}
    for i in range(len(f)):
        if is_tile_id(f[i]):
            ti[int(f[i][5:-1])] = [f[i+j] for j in range(1,edgelength+1)]
    return ti

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
        matches = 0
        for y in ed[x]:
            if y in erl or y in elr:
                matches += 1
        matches_per_tile[x] = matches
    return matches_per_tile

def read_edges_from_tile(input_tile):
    edges_out = []
    edges_out.append(''.join(input_tile[0]))
    edgelen = len(input_tile[0])
    edges_out.append(''.join([x[edgelen-1] for x in input_tile]))
    edges_out.append(''.join(input_tile[-1][::-1]))
    edges_out.append(''.join([x[0] for x in input_tile][::-1]))
    return edges_out

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

def flip_diagonal(mat):
    side = len(mat)
    mat_out = [['' for x in range(side)] for y in range(side)]
    for i in range(side):
        for j in range(side):
            mat_out[j][i] = mat[i][j] # side-j
    return mat_out

def flip_antidiagonal(mat):
    side = len(mat)
    mat_out = [['' for x in range(side)] for y in range(side)]
    for i in range(side):
        for j in range(side):
            mat_out[side-j-1][side-i-1] = mat[i][j] # side-j
    return mat_out

def flip_vertical(mat):
    side = len(mat)
    mat_out = [[] for y in range(side)]
    for i in range(side):
        mat_out[side-i-1] = mat[i] # side-j
    return mat_out

def flip_horizontal(mat):
    side = len(mat)
    mat_out = [['' for x in range(side)] for y in range(side)]
    for i in range(side):
        for j in range(side):
            mat_out[i][side-j-1] = mat[i][j] # side-j
    return mat_out

def print_two_tiles_LR(t0,t1):
    for i in range(len(t0)):
        print(''.join(t0[i]), ' ', ''.join(t1[i]))

def print_two_tiles_UD(t0,t1):
    for x in (t0,t1):
        for i in range(len(x)):
            print(''.join(x[i]))
        print('')

def atm(mat,pt,square): # add tiles to matrix
    tile = [x[1:-1] for x in square[1:-1]]
    (x,y) = pt
    x *= len(tile)
    y *= len(tile)
    for i in range(len(tile)):
        for j in range(len(tile[0])):
            mat[x+i][y+j] = tile[i][j]
    return mat

def find_orientation(sa, sb):
    if sa == sb:
        return 1
    if sa == sb[::-1]:
        return -1
    return 0

def orient_first_corner(a,b,c,d):
    take_to_east = [find_orientation(x, b) for x in a]
    take_to_south = [find_orientation(x, c) for x in a]
    if (take_to_east == [0,1,0,0] or take_to_east == [0,-1,0,0]):
        if (take_to_south == [1,0,0,0] or take_to_south == [-1,0,0,0]):
            return "flip vertical"
    if [take_to_east, take_to_south] == [[1, 0, 0, 0], [0, 0, 0, -1]]:
            return "flip antidiagonal"
    return "dunno"

def orient_RH_neighbour(a,b,c):
    LH = [find_orientation(x, a) for x in b]
    RH = [find_orientation(x, a) for x in c]
    print("In orient_RH_neigh.., LH, RH: ", LH, RH)
    if [LH, RH] == [[0, -1, 0, 0], [-1, 0, 0, 0]]:
        return 'flip over the main diagonal'
    if [LH, RH] == [[0, -1, 0, 0], [0, -1, 0, 0]]:
        return 'flip horizontal'
    if [LH, RH] == [[0, -1, 0, 0], [0, 0, 0, -1]]:
        return 'flip vertical'
    if [LH, RH] == [[0, -1, 0, 0], [0, 0, 1, 0]]:
        return 'flip antidiagonal, then vertical'
    if [LH, RH] == [[0, 1, 0, 0], [0, 0, 0, -1]]:
        return 'change nothing'
    if [LH, RH] == [[0, 1, 0, 0], [-1, 0, 0, 0]]:
        return 'flip over the main diagonal, then vertical'
    if [LH, RH] == [[0, 1, 0, 0], [0, 1, 0, 0]]:
        return 'flip horizontal'
    if [LH, RH] == [[0, 1, 0, 0], [0, 0, -1, 0]]:
        return 'flip over the main diagonal, then horizontal'
    if [LH, RH] == [[0, 1, 0, 0], [0, -1, 0, 0]]:
        return 'flip vertical, then horizonal'
    return [LH, RH]

'''
(Pdb) print_two_tiles_LR(tiles[pm[(0,0)]],tiles[pm[(0,1)]])
..##.####.   ....#.####
......#...   ...#.....#
..#....#.#   #.#....#.#
..##.....#   #.....#...
..##....#.   .......#..
#..#....#.   .......#.#
.#.....#.#   #....#..##
....#..#..   ...#.##.##
#..#......   .....#...#
#.##.##.##   ##.##.#...

print_two_tiles_LR(tiles[pm[(0,1)]],tiles[pm[(0,2 # Yes.
print_two_tiles_LR(tiles[pm[(0,2)]],tiles[pm[(0,3)]])
'''

def spinflip_tile(a,b):
    if a == 'flip horizontal':
        return flip_horizontal(b)
    if a == 'flip vertical':
        return flip_vertical(b)
    if a == 'change nothing':
        return b
    if a == 'flip antidiagonal':
        return flip_antidiagonal(b)
    if a == 'flip over the main diagonal':
        return flip_diagonal(b)
    if a == 'flip over the main diagonal, then vertical': # == rotate CCW pi/2.
        return flip_vertical(flip_diagonal(b))
    if a == 'flip over the main diagonal, then horizontal':
        return flip_horizontal(flip_diagonal(b))
    if a == 'flip vertical, then horizonal':
        return flip_horizontal(flip_vertical(b))
    if a == 'flip antidiagonal, then vertical':
        return flip_vertical(flip_antidiagonal(b))

def orient_southern_neighbour(a,b,c):
    North = [find_orientation(x, a) for x in b]
    South = [find_orientation(x, a) for x in c]
    if [North, South] == [[0, 0, -1, 0], [0, 0, -1, 0]]:
        return 'flip vertical'
    if [North, South] == [[0, 0, 1, 0], [0, 0, 1, 0]]:
        return 'flip vertical'
    if [North, South] == [[0, 0, -1, 0], [0, -1, 0, 0]]:
        return 'flip antidiagonal'
    if [North, South] == [[0, 0, 1, 0], [0, 1, 0, 0]]:
        return 'flip antidiagonal'
    if [North, South] == [[0, 0, 1, 0], [1, 0, 0, 0]]:
        return 'flip horizontal'
    if [North, South] == [[0, 0, 1, 0], [0, 0, 0, 1]]:
        return 'flip over the main diagonal'
    if [North, South] == [[0, 0, -1, 0], [0, 0, 0, -1]]:
        return 'flip over the main diagonal'
    if [North, South]== [[0, 0, 1, 0], [0, 0, -1, 0]]:
        return 'flip vertical, then horizonal'
    if [North, South]== [[0, 0, 1, 0], [0, -1, 0, 0]]:
        return 'flip over the main diagonal, then vertical'
    if [North, South]== [[0, 0, -1, 0], [0, 1, 0, 0]]:
        return 'flip over the main diagonal, then vertical'
    if [North, South]== [[0, 0, 1, 0], [0, 0, 0, -1]]:
        return 'flip over the main diagonal, then horizontal'
    if [North, South]== [[0, 0, -1, 0], [0, 0, 0, 1]]:
        return 'flip over the main diagonal, then horizontal'
    if [North, South]== [[0, 0, -1, 0], [-1, 0, 0, 0]]:
        return 'flip horizontal'
    if [North, South]== [[0, 0, -1, 0], [0, 0, 1, 0]]:
        return 'flip vertical, then horizonal'
    return [North, South]

infile = 'day20.txt'
with open(infile, 'r') as file:
    f = [x.strip() for x in file.readlines()]

ed = {int(x[5:-1]):[] for x in f if is_tile_id(x)}
read_0_edges(f,ed)
edgelength = len(ed[2311][0])
read_1_edges(f,ed,edgelength)
read_2_edges(f,ed,edgelength)
read_3_edges(f,ed,edgelength)
ma = count_matched_edges_per_tile(ed)
oc = [x for x in ma if ma[x] == 2] # Obligate corners.
print("Part 1", numpy.prod(oc), "if 4 = ", len(oc))
et = edt(ed)
ne = gr(et)
d00 = cd(ne,oc[0])
opposite = [x for x in d00 if d00[x]== max(d00.values())][0]
oc1 = [x for x in oc if x != oc[0] and x != opposite]
d01 = cd(ne, oc1[0])
d10 = cd(ne, oc1[1])
d1 = {x:(d00[x] + d01[x]-d00[oc1[0]])//2 for x in d00}
d0 = {x:(d00[x] + d10[x]-d00[oc1[0]])//2 for x in d00}
pm = invert_distance_to_tiles(d0,d1)
tiles = read_tiles(f,ed,edgelength)
final_size = (edgelength - 2) * (max(d0.values()) + 1)
mat = [['' for x in range(final_size)] for x in range(final_size)]
we = which_edge_matches(et,d0,d1)
print_two_tiles_LR(tiles[pm[(0,0)]],tiles[pm[(0,1)]])
print("joined on edge: ", we[(0.0,0.5)])

orient = orient_first_corner(ed[pm[(0,0)]],we[(0.0,0.5)],we[(0.5,0.0)],infile)
first_tile_flipped = spinflip_tile(orient,tiles[pm[(0,0)]])
tiles[pm[(0,0)]] = spinflip_tile(orient,tiles[pm[(0,0)]])
ed[pm[(0,0)]] = read_edges_from_tile(tiles[pm[(0,0)]])
mat = atm(mat,(0,0),tiles[pm[(0,0)]])

for i in range(1,max(d0.values())+1):
    orR = orient_RH_neighbour(we[(0.0,i-1+0.5)],ed[pm[(0,i-1)]],ed[pm[(0,i)]])
    print("i ", i, " orientation request", orR)
    if len(orR) == 2:
        breakpoint()
    tiles[pm[(0,i)]] = spinflip_tile(orR,tiles[pm[(0,i)]])
    ed[pm[(0,i)]] = read_edges_from_tile(tiles[pm[(0,i)]])
    mat = atm(mat, (0,i), tiles[pm[(0,i)]])

for i in range(1,max(d0.values())+1):
    for j in range(max(d0.values())+1):
        orR = orient_southern_neighbour(we[(i-0.5,j)],ed[pm[(i-1,j)]],ed[pm[(i,j)]])
        print("i ", i, "j ", j , " orientation request", orR)
        if len(orR) == 2:
            breakpoint()
        tiles[pm[(i,j)]] = spinflip_tile(orR,tiles[pm[(i,j)]])
        ed[pm[(i,j)]] = read_edges_from_tile(tiles[pm[(i,j)]])
        mat = atm(mat, (i,j), tiles[pm[(i,j)]])

seas = ['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   '] # Sea Serpent filter.
sealist = [(i,j) for i in range(len(seas)) for j in range(len(seas[0])) if seas[i][j] == '#']
#[(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19), (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]

for i in range(96):
    for j in range(96):
        if i + 3 in range(96):
            if j + 20 in range(96):
                if sum([1 for di in range(len(seas)) for dj in range(len(seas[0])) if mat[i+di][j+dj] == '#' and (di, dj) in sealist]) == 15:
                    for (di,dj) in sealist:
                        mat[i+di][j+dj] = 'O'

print_two_tiles_UD(mat,[[]])
print("part 2", sum([x.count('#') for x in mat]))
breakpoint()


'''
6 lines from the bottom:

..###...########..#####...##.....#.............##..#..........#...#..#..#.....#......#...#..##..
.#..####..#..#..#..##........#....##.#..##....#####.....#...#....##....##...####.......#.....#..
...#........##...#..#....#....#.##.##..#..#..#..#...##.......##.#..#..#..#..#...###.#..#....#..#

..#O#...OO####OO..##OOO...##.....#.............O#..#..........#...#..#..#.....O......#...#..##..
.#..O##O..O..O..O..O#........O....OO.#..OO....OOO##.....#...O....OO....OO...#OOO.......#.....#..
...#........##...#..#....#....O.#O.#O..O..O..O..#...##.......O#.O..O..O..O..O...###.#..#....#..#


['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ']

#print_two_tiles_UD(tiles[pm[(0,2)]], tiles[pm[(1,2)]])
#print_two_tiles_UD(tiles[pm[(0,2)]], tiles[pm[(1,2)]])
#print_two_tiles_LR(tiles[pm[(0,1)]], tiles[pm[(0,2)]])
'''
