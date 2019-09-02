
Weight = [0,1,2,5,2,5]
Value = [0,5,3,5,3,2]

Total = 10

# Let n be the number of items left to consider and capacity be the leftover capacity
# in the bag

dict = {}
def KS(n, capacity):
    key = str(n) + ":" + str(capacity)
    if key in dict.keys():
        return dict[key]

    if n == 0 or capacity == 0:
        result = 0
    elif Weight[n] > capacity:
        result = KS(n-1, capacity)
    else:
        temp1 = KS(n-1, capacity)
        temp2 = Value[n] + KS(n-1, capacity - Weight[n])
        result = max(temp1, temp2)
        dict[key] = result
        print(result)
    return result

print(KS(len(Weight)-1, Total))
