def moveAllToIethPosition2(input : str, targetPosition : int) -> int:
    return sum([abs(i - targetPosition) 
        for i, v in enumerate(input) if v == '1'])


def moveAllToIethPosition(input : str, targetPosition : int) -> int:
    result = 0 
    for i, v in enumerate(input):
        if v == "1":
            result += abs(i - targetPosition)
    return result

def computeSolutionVector(input : str) -> list[int]:
    #TODO: comment on aurait fait pour renvoyer un string?
    return [moveAllToIethPosition2(input[:], i) for i in range(len(input))]
    

print(computeSolutionVector("110"))
#Output: [1,1,3]
print(computeSolutionVector("001011"))
#Output: [11,8,5,4,3,4]
