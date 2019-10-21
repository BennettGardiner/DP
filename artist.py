# An artist has the possibility to visit a number of different exhibitions in different cities over
# the next four days. Based on her experience, she has estimated the probabilities of sales at
# each exhibition, given that she attends the exhibition for a day. Each of her paintings sells for
# $500. She also knows how much it costs to travel between exhibitions and from her home to
# each of the exhibitions. She can only attend each exhibition once.
# The data for sales and travel costs are given below.

Costs = [
    [0, 143, 108, 118, 121, 88, 121, 57, 92],     # Home
    [143, 0, 35, 63, 108, 228, 182, 73, 162],     # A
    [108, 35, 0, 45, 86, 193, 165, 42, 129],      # B
    [118, 63, 45, 0, 46, 190, 203, 73, 105],      # C
    [121, 108, 86, 46, 0, 172, 224, 98, 71],      # D
    [88, 228, 193, 190, 172, 0, 174, 160, 108],   # E
    [121, 182, 165, 203, 224, 174, 0, 129, 212],  # F
    [57, 73, 42, 73, 98, 160, 129, 0, 117],       # G
    [92, 162, 129, 105, 71, 108, 212, 117, 0]     # H
]

Sales = [
    [0.0, 0.0, 0.0],  # Home
    [0.3, 0.4, 0.3],  # A
    [0.2, 0.5, 0.3],  # B
    [0.2, 0.7, 0.1],  # C
    [0.3, 0.5, 0.2],  # D
    [0.3, 0.6, 0.1],  # E
    [0.4, 0.3, 0.3],  # F
    [0.0, 0.3, 0.7],  # G
    [0.1, 0.1, 0.8]   # H
]

Cities = range(len(Sales))

# The artist wants to maximize her expected profit from a tour of four exhibitions. What
# path should she take?

ExpectedValue = [500 * (0 * Sales[k][0] + 1 * Sales[k][1] + 2 * Sales[k][2]) for k in Cities]


def Artist(CurrentCity, AlreadyVisited):
    if len(AlreadyVisited) == 4:
        return (- Costs[CurrentCity][0], 0)
    Best = (- 999999, -1)
    for NextCity in Cities[1:]:
        if NextCity not in AlreadyVisited:
            Best = max(Best, (ExpectedValue[NextCity] - Costs[CurrentCity][NextCity]
                              + Artist(NextCity, AlreadyVisited | {NextCity})[0], NextCity)
                       )
    return Best


print(f"If number of paintings unlimited, \nTotal amount: ${Artist(0, set())[0]}")

city_list = [0]
for _t in range(4):
    city = Artist(city_list[-1], set(city_list))[1]
    city_list.append(city)
print(f"City path: {city_list}")

# Suppose now that the artist only has 5 paintings to sell. What is her optimal strategy
# for a tour of at most four exhibitions assuming that she will return home once all
# paintings are sold?

# We need to return a strategy rather than one answer, and track the number of paintings left in our state.
nCount = 0
def Artist2(CurrentCity, AlreadyVisited, PaintingsLeft):
    global nCount
    nCount += 1
    if len(AlreadyVisited) == 4 or PaintingsLeft == 0:
        return (-Costs[CurrentCity][0], 0)
    Best = (-999999, -1)
    for NextCity in Cities[1:]:
        if NextCity not in AlreadyVisited:
            ExpectedCost = -Costs[CurrentCity][NextCity]
            for s in range(3):
                ExpectedCost += Sales[NextCity][s] * \
                                (500 * min(s, PaintingsLeft) +
                                 Artist2(NextCity, AlreadyVisited | set([NextCity]), max(PaintingsLeft - s, 0))[0])
            Best = max(Best, (ExpectedCost, NextCity))
    return Best

print(f"If limited to 5 paintings, \nExpected amount: ${Artist2(0, set(), 5)[0]}")

cities = set()
p = 5
curr = 0

# If you have p paintings left where should you go?

for k in range(p, p-3, -1):
    print(f"Now at city {curr}. If you sell {k} paintings here, go to {Artist2(curr, cities, p)[1]}")

