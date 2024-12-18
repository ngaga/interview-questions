#TODO: try without slice copies

def getNextSmallerElement(ref : int, elementList : list[int]) -> int:
    for j in range(len(elementList)):
        if elementList[j] <= ref:
            return elementList[j]
    return 0


def computeDiscountsFromPrices(input : list[int]) -> list[int]:
    result = []
    for i in range(len(input)):
        price = input[i]
        result.append(price - getNextSmallerElement(price, input[i + 1:]))
    return result


print(computeDiscountsFromPrices([8,4,6,2,3]))
#[4,2,4,2,3]
print(computeDiscountsFromPrices([1,2,3,4,5]))
#[1,2,3,4,5]
print(computeDiscountsFromPrices([10,1,1,6]))
#[9,0,1,6]
