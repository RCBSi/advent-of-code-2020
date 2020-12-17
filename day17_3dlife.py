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

def matrix3d(Ma,Ne):
    ma = {x:'.' for x in Ne}
    for i in range(len(Ma)):
        for j in range(len(Ma[0])):
            ma[(i,j,0)] = Ma[i][j]
    return ma

def find_neighbours(M,le):
    neigh = defaultdict(set)
    ir = range(-le,len(M)+le)
    jr = range(-le,len(M[0])+le)
    kr = range(-le,le+1)
    for i in ir:
        for j in jr:
            for k in kr:
                for di in [-1,0,1]:
                    for dj in [-1,0,1]:
                        for dk in [-1,0,1]:
                            if (di,dj,dk) != (0,0,0):
                                (ip,jp,kp) = (i+di,j+dj,k+dk)
                                if ip in ir and jp in jr and kp in kr:
                                    neigh[(i,j,k)].add((ip,jp,kp))
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

def print_slice(Ma,xmin, xmax, ymin, ymax,z):
    for i in range(xmin,xmax+1):
        print(''.join([Ma[(i,j,z)]for j in range(ymin, ymax+1)]))

file = 'day17.txt'
steps = 6
Mat = read_matrix(file)
Nei = find_neighbours(Mat,steps)
M3d = [matrix3d(Mat,Nei)]
for i in range(steps):
    M3d.append(live(M3d[-1],Nei))
print([[M3d[k][x] for x in M3d[-1].keys()].count('#') for k in range(steps+1)])
breakpoint()
[M3d[-1][x] for x in M3d[-1].keys()].count('#')



breakpoint()
'''
advent-of-code-2020 ryan$ python lifecube1.py
[5, 11, 21, 38, 58, 101, 112]

(Pdb) print_slice(M3d[0],0,2,0,2,0)
.#.
..#
###

print_slice(M3d[1],0,3,0,3,-1)
....
#...
..#.
.#..
'''
#(Pdb) [x for x in M3d[0] if M3d[0][x] == '#']
#[(0, 1, 0), (1, 2, 0), (2, 0, 0), (2, 1, 0), (2, 2, 0)]

#x = [x for x in M3.keys()][1000]

# [M3d[x] for x in M3d].count('#')
# initially 5.
# [len(Nei[x]) for x in Nei]
# numpy.unique([len(Nei[x]) for x in Nei])
# array([ 7, 11, 17, 26
# (Pdb) [len(Nei[x]) for x in Nei].count(26)
# 1430
# (Pdb) [len(Nei[x]) for x in Nei].count(11)
# 136
# (Pdb) [len(Nei[x]) for x in Nei].count(17)
# 766
# [len(Nei[x]) for x in Nei].count(7)
# 8
#(Pdb) len([x for x in Nei])
#2700
#(Pdb) le = 6
#(Pdb) len(range(-le,len(Mat)+le))
#15
#(Pdb) len(range(-le,le))
#12
#(Pdb) 12*15*15
#2700
# M3d[(0,1,0)]
# '#'
