# Player A and B play a two game chess match, Player A
# has the following strategies each game,
# Bold: Pr(W) = 0.45, Pr(L) = 0.55, and
# Cons: Pr(D) = 0.9, Pr(L) = 0.1

# If the players are tied after two games they continue
# playing until one player wins a game.
# Maximise A's chance of winning the match.

bold = [0, 0.45, 0.55] # Draw, Win, Loss probabilities
cons = [0.9, 0, 0.1]
strategy = ["bold", "conservative"]

def V(t, s): # todo add memoization
    # print (t,s)
    if t >= 2 and s > 0:
        return (1, "you won!")
    if t >= 2 and s < 0:
        return (0, "you lost :(")
    if t == 3:
        return (bold[s], strategy[0])
    else:
        return max((a[1]*V(t+1,s+1)[0] + a[0]*V(t+1,s)[0] + a[-1]*V(t+1,s-1)[0], strat)
        for a, strat in [(bold, "bold"), (cons, "conservative")])

print('''
Player A's chances of winning the match are roughly %.2f%% \
if they use the %s strategy in the first game.
''' % (100* V(0,0)[0], V(0,0)[1])
)
