#WIIIIPPP
def maxNumberOfChunks(input : list[int]) -> int:
    result = 0
    print(sorted(input))
    if (sorted(input) == input):
        return 1
    return result


print(maxNumberOfChunks([1,0,2,3,4]))
print(maxNumberOfChunks([4,3,2,1,0]))
