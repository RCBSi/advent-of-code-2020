import re
with open('day18.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

def eval(s):
    if 'b' in s:
#        print("Removing b and following from ", s, " we got ", s[:s.index('b')])
        s = s[:s.index('b')]
    if re.search('\d+ \+ \d+',s):   # comment this and the following line for part 1. 
        return eval (re.sub('(\d+ \+ \d+)',maths,s))
    if '(' in s:
        return eval (re.sub('(\([^\(\)]+\))',maths,s))
    return maths(s)

def maths(mat):
#    print("We are requested to evaluate ", mat)
    if mat != str(mat):
        s = mat.group()
    else:
        s = mat
    if s:
        if s[0] == '(':
            s = s[1:]
        if s[-1] == ')':
            s = s[:-1]
        y = s.split()
#        print("Splitting ", s, " we got ", y)
        if y:
            out = int(y[0])
            y = y[1:]
            while y:
                op = y[0]
                ar = y[1]
                y = y[2:]
                if op == '*':
                    out *= int(ar)
                if op == '+':
                    out += int(ar)
            print(out)
            return str(out)
        else:
            return '0'
    else:
        return '0'

print([eval(s) for s in t])
breakpoint()
print(sum([int(eval(s)) for s in t]))
breakpoint()
