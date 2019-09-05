# A company knows that the demand for its product during each of the next four
# months will be as follows:

# Months 1 2 3 4
# Demand 2 3 2 4

# At the beginning of each month, the company must determine how many units
# should be produced during the current month. During a month in which units are
# produced, a setup cost of $3 is incurred. In addition, there is a variable cost of $1
# for every unit produced. At the end of each month, a holding cost of 50 cents per
# unit on hand is incurred. Capacity limitations allow a maximum of 5 units to be
# produced during each month. The size of the company’s warehouse restricts the
# ending inventory of each month to at most 4 units.

# How many units should the company produce each month to satisfy demand and
# minimise total cost?

D = {1: 2, 2: 3, 3: 2, 4: 4}

def f(x):
    if x==0:
        return 0
    else:
        return 3+x

_V = {}
def V(t, s):
    print(t,s)
    if (t,s) not in _V:
        if t==5:
            _V[t,s] = (0,0)
        else:
            _V[t,s] = min((f(a)+0.5*(s+a-D[t])+V(t+1,s+a-D[t])[0],a) for
                   a in range(max(0,D[t]-s),min(5,4+D[t]-s)+1))
    return _V[t,s]

print(V(1,0))
