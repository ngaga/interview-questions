def numberOfSums(input : list[int], target) -> int:
    def rec(remaining : list[int], sum : int) -> None:
        print("Sum ", sum)
        nonlocal result
        if remaining:
            pop = remaining.pop()
            rec(remaining[:], sum+pop)
            rec(remaining[:], sum-pop)
        else:
            if sum == target:
                result += 1
            return
    result = 0
    rec(input[:], 0) 
    return result


print(numberOfSums([2,1], 1))
print(numberOfSums([1,1,1,1,1], 3))
print(numberOfSums([1], 1))


