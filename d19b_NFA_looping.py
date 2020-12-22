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

def test_lang_cross1(word, l1, l2, len1, len2):
    if len(word) ==  len1 + len2:
        if word[:len1] in l1:
            if word[len1:] in l2:
                return 1
    return 0

def test_lang_cross(word, l1, l2, n): #n == 8
    if len(word) < n*3:
        return 0
    bars = [word[i:i+n] for i in range(0,len(word),n)]
    for i in range(len(bars)):
        if i > len(bars)//2:
            if not([x for x in bars[:i] if not(x in l1)]):
                if not([x for x in bars[i:] if not(x in l2)]):
                    return 1
#        print(i, not([x for x in bars[:i] if not(x in l1)]), not([x for x in bars[i:] if not(x in l2)]))
    return 0


    for w in [word[i:i+n] for i in range(0,len(word),n)][:-1]:
        if w not in l1:
            return 0
    if word[-n:] not in l2:
            return 0
    return 1

rules = [x for x in t if character_or_not(x) in [str(x) for x in range(10)]]
sm = {a:b for [a,b] in [r.split(': ') for r in rules]} # statemap from state to states.
smk = [int(x) for x in sm]
smk.sort()
smk == range(len(smk))
print("The rules are indexed by the first n numbers: ", [x for x in range(0,len(smk))] == smk)
test_words = [x for x in t if character_or_not(x) in ('a','b')]
l1 = language('42')
l2 = language('31')
#langlen = {x:len(language(x)) for x in sm if depth(x) < 11}
#print("Is the language of 0 the product of languages 8 and 11 ? ", langlen['11']*langlen['8'] == langlen['0'])
nlen = min([len(x) for x in language('42')])
print("part2 :", sum([test_lang_cross(x, language('42'), language('31'), nlen) for x in test_words]))
breakpoint()


breakpoint()
'''
[test_lang_cross1(x, language('8'), language('11'), 5, 10) for x in test_words]
[x for x in test_words if test_lang_cross1(x, language('8'), language('11'), 5, 10)]
[x for x in test_words if test_lang_cross(x, language('42'), language('31'), nlen)]
Here we see three succeed
bbabbbbaabaabba, ababaaaaaabaaab, and ababaaaaabbbaba
bbabbbbaabaabba, ababaaaaaabaaab, and ababaaaaabbbaba

['bbabbbbaabaabba', 'bbbbbbbaaaabbbbaaabbabaaa', 'ababaaaaaabaaab', 'ababaaaaabbbaba', 'abbbbabbbbaaaababbbbbbaaaababb', 'aaaaabbaabaaaaababaa']
['bbabbbbaabaabba', 'babbbbaabbbbbabbbbbbaabaaabaaa', 'aaabbbbbbaaaabaababaabababbabaaabbababababaaa','bbbbbbbaaaabbbbaaabbabaaa','bbbababbbbaaaaaaaabbababaaababaabab','ababaaaaaabaaab','ababaaaaabbbaba','baabbaaaabbaaaababbaababb','abbbbabbbbaaaababbbbbbaaaababb','aaaaabbaabaaaaababaa','aaaabbaabbaaaaaaabbbabbbaaabbaabaaa','aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba']
[x for x in we_find if x not in they_find]

['aaaabbaabbaaaaaaabbbabbbaaabbaabaaa', 'aaabbbbbbaaaabaababaabababbabaaabbababababaaa', 'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba', 'baabbaaaabbaaaababbaababb', 'babbbbaabbbbbabbbbbbaabaaabaaa', 'bbbababbbbaaaaaaaabbababaaababaabab']
word = 'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa'
bars = [word[i:i+5] for i in range(0,len(word),5)]
['aaaab', 'baabb', 'aaaaa', 'aabbb', 'abbba', 'aabba', 'abaaa']

[len(x) for x in language('11')].count(16)
16384
(Pdb) len([len(x) for x in language('11')])

length of a successful word is then always 24.


NFA = Nondeterministic finite automata.
They are written this way.
Dana Scott showed DFA = NFA, i.e., deterministic finite automata accept the same languages.

The codes are states.
In state 12, you accept iff the next letter is "a".
In state 23 you accept just in case:
    switch state to 12 and accept and then 112 and accept, or
    switch state to 7 and acceppt and then 38 and accept.

write it as recursion

test_lang0(x) for x in test_words]

[0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]

'''
