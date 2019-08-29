# A comparison of methods of calculating the Fibonacci numbers
# using naive recursion, memoization and a bottom-up approach

# Naive recursion approach
def fib(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Momoize function
def fib_memo(n, M = {1:1, 2:1}):
    if n in M.keys():
        return M[n]
    else:
        M[n] = fib_memo(n-1, M) + fib_memo(n-2, M)
        return M[n]

# A bottom up approach
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    else:
        bottom_up = []
        bottom_up.append(1)
        bottom_up.append(1)
        for i in range(2, n):
            bottom_up.append(bottom_up[i-1] + bottom_up[i-2])
    return bottom_up[-1]

print(fib_bottom_up(10000))
