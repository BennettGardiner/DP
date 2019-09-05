
# Maximise the function (x0 + 5)(x1 + 1)(x2 + 2)(x3 + 1) subject to
# 3x0 + 2x1 + x2 + x3 <= 8, where all variables are non-negative integers

consts = [5, 1, 2, 1]
coeffs = [3, 2, 1, 1]
T = 8

_V = {}


def V(t, s):
    if not (t, s) in _V:
        if t >= len(consts):
            _V[t, s] = (1, 0)
        else:
            _V[t, s] = max(
                ((a + consts[t]) * V(t + 1, s + coeffs[t] * a)[0], a) for a in range(int((T - s) / coeffs[t]) + 1))
    return _V[t, s]


def find_solutions(t, s):
    max_val = V(t, s)[0]

    if t >= len(consts):
        yield []
    else:
        for a in range(int((T - s) / coeffs[t]) + 1):
            if (a + consts[t]) * V(t + 1, s + coeffs[t] * a)[0] == max_val:
                for b in find_solutions(t + 1, s + coeffs[t] * a):
                    yield [a] + b


print(V(0, 0))
for sol in find_solutions(0, 0):
    print(sol)
