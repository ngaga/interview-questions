
#complexity -> probably in O(n) because inserting and looking in dict is O(1) #TODO: check
def findMostFrequent(a):
    valueToCount = {}
    for e in a:
        if e in valueToCount:
            valueToCount[e] += 1
        else:
            valueToCount[e] = 1
    maxCount = 0
    resKey = 0
    for k in valueToCount:
        if maxCount < valueToCount[k]:
            resKey = k
            maxCount = valueToCount[k]
    return resKey
    



a = [1,2,2,2,2,2,4,6,8, 65, 88,94,132,2,2,2,2,2,2999,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
c = findMostFrequent(a)
print("freq", c)
