import numpy
from collections import defaultdict

def find_neighbors(M):
    neigh = defaultdict(set)
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'L':
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        if (k,l) != (0,0):
                            seek = 1
                            while seek:
                                ip = i+k*seek
                                jp = j+l*seek
#                                print(" (",ip,",",jp,"), ")
                                if ip >= 0 and ip < len(M) and jp >= 0 and jp < len(M[0]):
                                    if M[ip][jp] == 'L':
                                        neigh[(i,j)].add((ip,jp))
                                        seek = 0
                                    else:
                                        seek += 1
                                else:
                                    seek = 0
    return neigh

def Occ(M,s):
    return [M[a][b] for (a,b) in s].count('#')

def read_matrix(filename):
    Ma = []
    with open(filename, 'r') as file:
        for x in file.readlines():
            y = list(x.strip())
            Ma.append(y)
    return Ma

def live_or_die2(cha,ct):
    if cha == '#' and ct >= 5:
        return 'L'
    if cha == 'L' and ct == 0:
        return '#'
    return cha

def live(Mat, Nei, ag):
    Mat.append([[live_or_die2(Mat[ag][i][j],Occ(Mat[ag],Nei[(i,j)])) for j in range(len(Mat[ag][i]))] for i in range(len(Mat[ag]))])
    return ag+1

def print_grid(Mat, date):
    for i in range(len(Mat[date])):
        print(''.join(Mat[date][i]))

file = 'day11.txt'
Mat = [read_matrix(file)]
Nei = find_neighbors(read_matrix(file))
ag = live(Mat, Nei, 0)
while Mat[ag-1] != Mat[ag]:
    ag = live(Mat, Nei, ag)
#    print(sum([x.count('#') for x in Mat[ag]]))
#    print_grid(Mat,ag)
print("part 2 : ", sum([x.count('#') for x in Mat[ag]]))
breakpoint()
