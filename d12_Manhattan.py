with open('day12.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

def simplify_spins(x):
    if x == 'R270':
        return 'L90'
    if x == 'L270':
        return 'R90'
    if x == 'R180':
        return 'L180'
    return x

def mapf(direc, orien):
    orien = orien%4
    if direc == 'F' and orien == 0:
        return 'E'
    if direc == 'F' and orien == 1:
        return 'N'
    if direc == 'F' and orien == 2:
        return 'W'
    if direc == 'F' and orien == 3:
        return 'S'
    return direc

def dx(direc, argu):
    if direc == 'E':
        return argu
    if direc == 'W':
        return -1 * argu
    return 0

def dy(direc, argu):
    if direc == 'N':
        return argu
    if direc == 'S':
        return -1 * argu
    return 0

def mk_orient(dir, arg):
    ori = [0]
    for i in range(len(dir)):
        orie = ori[-1]
        if dir[i] == 'R':
            orie -= arg[i]//90
        if dir[i] == 'L':
            orie += arg[i]//90
        ori = ori+[orie]
    return [x%4 for x in ori]

def mk_waypo(t):
    ori_x = [10]
    ori_y = [1]
    for i in range(len(t)):
        orix = ori_x[-1]
        oriy = ori_y[-1]
        if t[i] == 'R90':
            (orix,oriy) = (ori_y[-1], -1*ori_x[-1])
        if t[i] == 'L90':
            (orix,oriy) = (-1*ori_y[-1], ori_x[-1])
        if t[i] == 'L180':
            (orix,oriy) = (-1*ori_x[-1], -1*ori_y[-1])
        orix += dx(t[i][0],arg[i])
        oriy += dy(t[i][0],arg[i])
        ori_x = ori_x + [orix]
        ori_y = ori_y + [oriy]
    return [ori_x, ori_y]

def moveF(instru, argu, wayp):
    if instru[0] == 'F':
        return wayp * argu
    return 0

t = [simplify_spins(x) for x in t]
dir = [x[0] for x in t]
arg = [int(x[1:]) for x in t]
# ori = mk_orient(dir, arg)
#dir2 = [mapf(dir[i],ori[i]) for i in range(len(dir))]
#print("part1 ", abs(sum([dx(dir2[i],arg[i]) for i in range(len(dir))])) +
#abs(sum([dy(dir2[i],arg[i]) for i in range(len(dir))])))
ori = mk_waypo(t)
for i in range(len(t)):
    print(ori[0][i], ori[1][i], t[i], moveF(t[i], arg[i], ori[0][i]), moveF(t[i], arg[i], ori[1][i]))
print("part 2: ", abs(sum([moveF(t[i], arg[i], ori[0][i]) for i in range(len(t))])) + abs(sum([moveF(t[i], arg[i], ori[1][i]) for i in range(len(t))])))    
breakpoint()
#[i for

