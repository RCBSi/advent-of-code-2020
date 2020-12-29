pk = [19241437, 17346587] # public keys.
p1 = 20201227

def find_exponent(desired):
    purepowermodp = 1
    for i in range(p1):
        if purepowermodp == desired:
            return i
        purepowermodp = purepowermodp*7%p1

e = find_exponent(pk[0])
e1 = find_exponent(pk[1])
print("part1", 7**(e1*e%(p1-1))%p1)
