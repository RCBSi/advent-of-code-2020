import numpy
with open('day13.txt', 'r') as file:
    f = [x.strip() for x in file.readlines()]

start = int(f[0])
end = [int(x) for x in f[1].split(',') if x != 'x']
wait = min([x - start%x for x in end])
print("part 1 : ", [x for x in end if x - start%x == wait][0]*wait)
cond = f[1].split(',')
con = [(int(cond[i]),i) for i in range(len(cond)) if cond[i] != 'x']
con = [(int(cond[i]),int(cond[i])-i) for i in range(len(cond)) if cond[i] != 'x']
con.sort(reverse=True)
# without x-i : [(937, 17), (397, 48), (41, 7), (37, 54), (29, 46), (23, 40), (19, 67), (17, 0), (13, 35)]
# [(937, 920), (397, 349), (41, 34), (37, -17), (29, -17), (23, -17), (19, -48), (17, 17), (13, -22)]
(m,ax) = con[0]
res = ax
solved = [con[0]]
con = con[1:]

while con:
    (ch,ay) = con[0]
    ay = ay%ch
    if len(numpy.unique([(res + m*i)%ch for i in range(ch)])) < ch:
        print(numpy.unique([(res + m*i)%ch for i in range(ch)]))
    timer2 = 0
    while res%ch != ay and timer2 < ch*3:
        res += m
        timer2 += 1
    solved.append(con[0])
    print("Res ", res, " satisfies solved ", [res%a==b%a for (a,b) in solved])
    m *= ch
    con = con[1:]

breakpoint()
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# [(2409044 + m*i)%ch for i in range(ch
