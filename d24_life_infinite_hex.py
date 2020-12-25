import numpy
'''
For part 1, day 24 we identified tile locations.
For part 2, we have to identify the whole graph of neighbors as in the life game.

expand_neighbors(neighbors, live tiles : if the live tiles are not in the neighbors' dictionary, add them!).
occurrences. (from a set of live tiles and the set of neighbors of x, compute the # of live neighbors of x).
    if we look up the neighbors in the set of live tiles, the lookup can be slow.
    alternately, we expand the universe and store a dict of who is alive, who dead.

'''
with open('day24.txt', 'r') as file:
    f = [x.strip() for x in file.readlines()]

def av(z,zz): #vector addition
    return [z[0]+zz[0], z[1]+zz[1]]

def parse(path):
    i = 0
    parsed = []
    while i in range(len(path)):
        if path[i] in ['n','s']:
            parsed.append(path[i:i+2])
            i+= 2
        else:
            parsed.append(path[i:i+1])
            i+= 1
    return parsed

def locate(st):
    step_array = parse(st)
    z = [0,0]
    for w in step_array:
        z = av(z,ve[w])
    return z

ve = {
    'nw': [-0.5, 1],'ne': [0.5, 1], #There's no need to put sqrt(3) here.
    'e': [1,0], 'w':[-1,0],
    'sw': [-0.5, -1],'se': [0.5, -1]}

def pn(z): # neighbors of the hexagon z.
    return [av(z,ve[v]) for v in ve]

def cln(lt, z): # count_live_neighbors of a tile
    return len([x for x in pn(z) if x in lt])

def uniq(inarr):
    return [[y for y in x] for x in numpy.unique(inarr, axis=0)]

def play_once(black_tile_input):
    but = uniq(black_tile_input)
    wt = uniq([y for z in but for y in pn(z) if not (y in but)])
    wb = [x for x in wt if cln(but,x) == 2]
    bb = [x for x in but if cln(but,x) in (1,2)]
    return wb+bb

t = [locate(x) for x in f]
print("part 1",  len([x for x in t if t.count(x)%2]))
black_tiles = [[x for x in t if t.count(x)%2]]
breakpoint()
for i in range(1,101):
    black_tiles.append(play_once(black_tiles[-1]))
    print(i, len(black_tiles[-1]))
print("Part2:",len(black_tiles[-1]))
breakpoint()
