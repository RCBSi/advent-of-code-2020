with open('day21.txt', 'r') as file:
    f = [x.strip() for x in file.readlines()]

from collections import defaultdict
ai = defaultdict(set) # allergen to items that might contain that allergen.

def reduce_potential_ingredients(ing,al):
    if ai[al]:
        ai[al] = ai[al].intersection(ing)
    if not(ai[al]):
        ai[al] = set(ing)

def update_allergen_to_item_dictionary(clause,uni):
    ingredients = clause.split( '(' )[0].split()
    allergens = clause.split( '(' )[1][:-1].split()[1:]
    allergens = [x.replace(',','') for x in allergens]
#    breakpoint()
    for al in allergens:
        reduce_potential_ingredients(ingredients,al)
    return uni.union(ingredients)

uni = set()
for x in f:
    uni = update_allergen_to_item_dictionary(x,uni)

for x in ai:
    for y in ai[x]:
        if y in uni:
            uni.remove(y)
sets = [g for g in ai.values()]

can_have_allergen = sets[0].union(*sets)
cts = [sum([1 for fl in f if al in fl.split( '(' )[0].split()]) for al in uni]

print("part 1", sum(cts))
