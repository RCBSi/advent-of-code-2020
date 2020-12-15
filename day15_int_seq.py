inp = [12,1,16,3,11,0]
bd = {inp[i]:i for i in range(len(inp))}

def play(bd,la,t):
    if la in bd:
        return (t-1, t-1-bd[la], t+1)
    else:
        return (t-1, 0, t+1)

(la, t) = (inp[-1], len(inp))
for i in range(30000000-len(inp)):
    if i == 2020-len(inp):
        print("part 1:", la)
    (bd[la], la, t) = play(bd, la, t)

print("part 2: ", la)
