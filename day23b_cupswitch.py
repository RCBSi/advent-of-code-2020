def create_successor(seq):
    top = 1000000 #20 #1000000
    succ = {int(seq[i]):int(seq[i+1]) for i in range(len(seq)) if i+1 in range(len(seq))}
    succ[int(seq[-1])]=len(seq)+1
    extra = range(len(seq)+1,top+1)
    succ = succ | {i:i+1 for i in extra if i+1 in extra}
    succ[top] = int(seq[0])
    return succ

def successor_to_sequence(succ, init):
    out = str(init)
    for i in range(len(succ)-1):
        init = succ[init]
        out += str(init)
    return out

def pick_up_cups(succ, active):
    pick_up = [succ[active]]
    for i in range(2):
        pick_up.append(succ[pick_up[-1]])
    return pick_up

def subtract_one(succ, active):
    if active-1 in succ:
        d = active-1
    else:
        d = max(succ.keys())
    return d

def choose_destination(active, succ, pu):
    d = subtract_one(succ, active)
    while d in pu:
        d = subtract_one(succ, d)
    return d

def change_successor(succ, active, d, pu):
    if pu[-1] in succ and active in succ and d in succ:
        succ[active] = succ[pu[-1]]
        succ[pu[-1]] = succ[d]
        succ[d] = pu[0]
#        print("len succ now ", len(succ))
    else:
        print("Surprisingly, succ doesn't contain active, pu[-1] and d")
        print("pu[-1] in succ", pu[-1] in succ)
        print("active in succ", active, active in succ)
        print("d in succ", d, d in succ)
    return succ[active]

def play_cups_once(succ, active):
    pu = pick_up_cups(succ, active)
    dest = choose_destination(active, succ, pu)
#    print(successor_to_sequence(succ,3), "pickup", pu, "destination", dest)
    return change_successor(succ, active, dest, pu)

input = '389125467'
input = '643719258'
succ = create_successor(input)
print("The inverters work, right?", input == successor_to_sequence(succ,3))
active = int(input[0])
for i in range(10000000):
#    print(successor_to_sequence(succ,3), active)
    active = play_cups_once(succ, active)
#print("Final", successor_to_sequence(succ,3), "active", active)
#print("Part 1", successor_to_sequence(succ,1)[1:])
print("Part 2", succ[succ[1]] * succ[1])
breakpoint()
