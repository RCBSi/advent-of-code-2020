import numpy
from collections import defaultdict

def live_or_die2(cha,ct):
    if cha == '#' and ct >= 5:
        return 'L'
    if cha == 'L' and ct == 0:
        return '#'
    return cha

def read_matrix(filename):
    Ma = []
    with open(filename, 'r') as file:
        for x in file.readlines():
            y = list(x.strip())
            Ma.append(y)
    return Ma

def matrix4d(Ma,Ne):
    ma = {x:'.' for x in Ne}
    for i in range(len(Ma)):
        for j in range(len(Ma[0])):
            ma[(i,j,0,0)] = Ma[i][j]
    return ma

def find_neighbours(M,le):
    neigh = defaultdict(set)
    ir = range(-le,len(M)+le+1)
    jr = range(-le,len(M[0])+le+1)
    kr = range(-le,le+1)
    lr = range(-le,le+1)
    for i in ir:
        for j in jr:
            for k in kr:
                for l in lr:
                    for di in [-1,0,1]:
                        for dj in [-1,0,1]:
                            for dk in [-1,0,1]:
                                for dl in [-1,0,1]:
                                    if (di,dj,dk,dl) != (0,0,0,0):
                                        (ip,jp,kp,lp) = (i+di,j+dj,k+dk,l+dl)
                                        if ip in ir and jp in jr and kp in kr and lp in lr:
                                            neigh[(i,j,k,l)].add((ip,jp,kp,lp))
    return neigh

def CtNei(M,s): #Count neighbors which are alive.
    return [M[x] for x in s].count('#')

def live(M3, Ne):
    return {x:live_or_die(M3[x],CtNei(M3,Ne[x])) for x in M3.keys()}

def live_or_die(cha,ct):
    if cha == '#':
        if ct in (2,3):
            return '#'
        else:
            return '.'
    if cha == '.':
        if ct == 3:
            return '#'
        else:
            return '.'

def print_slice(Ma,xmin, xmax, ymin, ymax,z,w):
    for i in range(xmin,xmax+1):
        print(''.join([Ma[(i,j,z,w)]for j in range(ymin, ymax+1)]))

file = 'day17.txt'
steps = 6
Mat = read_matrix(file)
Nei = find_neighbours(Mat,steps)
M3d = [matrix4d(Mat,Nei)]
for i in range(steps):
    M3d.append(live(M3d[-1],Nei))
print([[M3d[k][x] for x in M3d[-1].keys()].count('#') for k in range(steps+1)])
breakpoint()
[M3d[-1][x] for x in M3d[-1].keys()].count('#')



breakpoint()

'''
(Pdb) print_slice(M3d[0],0,2,0,2,0,0)
.#.
..#
###

(Pdb) print_slice(M3d[1],0,3,0,3,-1,-1) # NB: must increase 2 to 3 to see the active cells shift this to 

test: [5, 29, 60, 320, 188, 1056, 680]
real: [36, 111, 255, 708, 520, 1616, 2332]

CtNei(M3d[0],Nei[(0,1,-1,-1)])
2

With 2 it should not com to life.

print_slice(M3d[0],-1,1,-1,1,0,0)

 With the toy example day17a, we expect toi see 848 cubes at the end, but
 my simulation gives: [5, 29, 60, 320, 188, 1056, 680]
 Hence,
 part 2: 1912 That's not the right answer; your answer is too low.
(Pdb) [x for x in M3d[0] if M3d[0][x] == '#']
[(0, 1, 0), (1, 2, 0), (2, 0, 0), (2, 1, 0), (2, 2, 0)]

x = [x for x in M3.keys()][1000]

 [M3d[x] for x in M3d].count('#')
 initially 5.
 [len(Nei[x]) for x in Nei]
 numpy.unique([len(Nei[x]) for x in Nei])
 array([ 7, 11, 17, 26
 (Pdb) [len(Nei[x]) for x in Nei].count(26)
 1430
 (Pdb) [len(Nei[x]) for x in Nei].count(11)
 136
 (Pdb) [len(Nei[x]) for x in Nei].count(17)
 766
 [len(Nei[x]) for x in Nei].count(7)
 8
(Pdb) len([x for x in Nei])
2700
(Pdb) le = 6
(Pdb) len(range(-le,len(Mat)+le))
15
(Pdb) len(range(-le,le))
12
(Pdb) 12*15*15
2700
 M3d[(0,1,0)]
 '#'
'''
