# Solves the problem of finding the number of subsets of an array of positive integers
# that add to a given integer, using recursion and dynamic programming.

set_nums = [2,4,6,10]
total = 16

# Recursive method

def rec(array, total, i, mem = {}):
    # Remove the ith term in the array, then consider subsets of the remaining
    # terms that add to either the total or the total - this term
    key = str(total) + ':' + str(i)
    if key in mem:
        return mem[key]

    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < array[i]:
        to_return = rec(array, total, i-1, mem)
    else:
        to_return = rec(array, total, i-1, mem) + rec(array, total - array[i], i-1, mem)
        mem[key] = to_return
        return to_return

print(rec(set_nums, total, len(set_nums)-1))
