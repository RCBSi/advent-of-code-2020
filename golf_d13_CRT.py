with open('day13.txt', 'r') as file:
    f = [x.strip() for x in file.readlines()]

start = int(f[0])
end = [int(x) for x in f[1].split(',') if x != 'x']
wait = min([x - start%x for x in end])
print("part 1 : ", [x for x in end if x - start%x == wait][0]*wait)
cond = f[1].split(',')
con = [(int(cond[i]),int(cond[i])-i) for i in range(len(cond)) if cond[i] != 'x']
con.sort(reverse=True)
(m,res) = con[0]
con = con[1:]

while con:
    (ch,ay) = con[0]
    while res%ch != ay%ch:
        res += m

    m *= ch
    con = con[1:]

print("part 2 : ", res)
