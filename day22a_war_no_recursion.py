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

def play_war(game):
    if game_over(game):
        return game
    else:
        alice = game[0]
        bob = game[1]
        index = game[2]
        for (a,b) in ((alice, bob), (bob,alice)):
            if a[index] > b[index]:
                a.append(a[index])
                a.append(b[index])

        return [alice, bob, index+1]

def score(deck):
    deck.reverse()
    return [deck[i]*(i+1) for i in range(len(deck))]


alice = read_hand(t,1)
bob = read_hand(t,2)
game = [alice, bob, 0]
while not(game_over(game)):
    print(game[0][game[2]:], game[1][game[2]:])
    game = play_war(game)
print(sum(score(game[winner_is(game)][game[2]:])))

