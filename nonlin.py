# Maximise the function (x1 + 5)(x2 + 1)(x3 + 2) subjec to
# 3x1 + 2x2 + x3 <= 6, where all variables are non-negative integers

c = [5, 1, 2]
d = [3, 2, 1]
T = 6

def V(t,s):
    if t == 3:
        return (1, 0)
    else:
        return max(((a + c[t]) * V(t + 1, s + d[t] * a)[0], a) for a in range(int((T - s)/ d[t]) + 1))

print(V(2,4))
