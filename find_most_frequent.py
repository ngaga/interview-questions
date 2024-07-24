
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

#correction from Dust's codding buddy : almost the same? init at none if array is empty is better. Update on the fly seems less
def most_frequent_item(arr):
    # Utilizing a dictionary for counting occurrences
    count = {}
    max_count = 0
    most_frequent = None
    
    # O(n) time complexity for one pass of the array
    for item in arr:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
        
        # Update most frequent item on the fly
        if count[item] > max_count:
            max_count = count[item]
            most_frequent = item
    
    return most_frequent

# Overall complexity: O(n) time, O(k) space where k is the number of distinct items

