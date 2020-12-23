import re
with open('day19.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

def character_or_not(x):
    if x:
        return x[0]
    else:
        return x

[character_or_not(x) for x in t]

def accept(state,string):
    return 1

def depth(rulenum):
    if rulenum in sm:
        return max([depth(x) for x in sm[rulenum].split()])+1
    else:
        return 0

def language(nfa):
    if nfa in ('"a"','"b"'):
        return nfa[1]
    if nfa in ('a','b'):
        return [nfa]
    if re.findall(' \| ',nfa):
        return [y for x in nfa.split(' | ') for y in language(x)]
    else:
        if nfa in sm:
            return language(sm[nfa])
        if re.findall(' ',nfa):
            first = nfa.split()[0]
            second = nfa.split()[1]
            return [x+y for x in language(first) for y in language(second)]

rules = [x for x in t if character_or_not(x) in [str(x) for x in range(10)]]

def test_lang_cross(word, l1, l2, len1, len2):
    if len(word) ==  len1 + len2:
        if word[:len1] in l1:
            if word[len1:] in l2:
                return 1
    return 0

sm = {a:b for [a,b] in [r.split(': ') for r in rules]} # statemap from state to states.
smk = [int(x) for x in sm]
smk.sort()
smk == range(len(smk))
print("The rules are indexed by the first n numbers: ", [x for x in range(0,len(smk))] == smk)
test_words = [x for x in t if character_or_not(x) in ('a','b')]
l1 = language('8')
l2 = language('11')
#langlen = {x:len(language(x)) for x in sm if depth(x) < 11}
#print("Is the language of 0 the product of languages 8 and 11 ? ", langlen['11']*langlen['8'] == langlen['0'])
print("part1 :", sum([test_lang_cross(x, l1, l2, 8, 16) for x in test_words]))
breakpoint()
