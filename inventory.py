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
