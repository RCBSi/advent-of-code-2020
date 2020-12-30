def find_exponent(desired):
    purepowermodp = 1
    for i in range(p1):
        if purepowermodp == desired:
            return i
        purepowermodp = purepowermodp*7%p1

[pk,p1] = [[19241437, 17346587],20201227] # public keys, prime modulus.
(e,e1) = (find_exponent(pk[0]),find_exponent(pk[1]))
print("part1", 7**(e1*e%(p1-1))%p1)
