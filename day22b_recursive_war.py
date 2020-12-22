with open('day22.txt', 'r') as file:
    t = [x.strip() for x in file.readlines()]

def read_hand(t,rank):
    ctp = 0
    hand = []
    for x in t:
        if x:
            if x[0] == 'P':
                ctp += 1
            else:
                if ctp == rank:
                    hand.append(int(x))
    return hand

def game_over(game):
    for i in (0,1):
        if game[2] >= len(game[i]):
            return 1
    return 0

def winner_is(game):
    for i in (0,1):
        if game[2] >= len(game[i]):
            return 1-i
    return -1

def dont_play_recursive(game):
    for i in (0,1):
        if len(game[i][game[2]+1:]) < game[i][game[2]]:
            return 1
    return 0

def play_war(game):
    if game_over(game):
        return game
    else:
        alice = game[0]
        bob = game[1]
        index = game[2]
        if (dont_play_recursive(game)):
            for (a,b) in ((alice, bob), (bob,alice)):
                if a[index] > b[index]:
                    a.append(a[index])
                    a.append(b[index])

            return [alice, bob, index+1]
        else:
            res = play_combat(game)
            if res == 0:
                alice.append(alice[index])
                alice.append(bob[index])
            if res == 1:
                bob.append(bob[index])
                bob.append(alice[index])
            if res == -1:
                print("I did not expect that.")
            return [alice, bob, index+1]

def play_combat(game):
    alice = game[0][game[2]+1:][:game[0][game[2]]]
    bob = game[1][game[2]+1:][:game[1][game[2]]]
    subgame = [alice, bob, 0]
    subrepeats = {}
    while not(game_over(subgame)) and not(table(subgame) in subrepeats): #and not(table(subgame) in repeats):
        tst= table(subgame)
#        print(tst)
        subrepeats[table(subgame)] = 1
        repeats[table(subgame)] = 1
        subgame = play_war(subgame)
#    if table(subgame) in repeats:
#        return 0
    if table(subgame) in subrepeats:
        return 0
    return winner_is(subgame)

def score(deck):
    deck.reverse()
    return [deck[i]*(i+1) for i in range(len(deck))]

def visible(deck,i):
    return ','.join([str(x) for x in deck[i:]])

def table(game):
    return visible(game[0],game[2])+'V' + visible(game[1],game[2])

alice = read_hand(t,1)
bob = read_hand(t,2)
game = [alice, bob, 0]
repeats = {}
while not(game_over(game)) and not(table(game) in repeats):
    tst= table(game)
#    print(tst)
    repeats[tst] = 1
    game = play_war(game)
if game_over(game):
    print(sum(score(game[winner_is(game)][game[2]:])))
if table(game) in repeats:
    print(sum(score(game[0][game[2]:])))

