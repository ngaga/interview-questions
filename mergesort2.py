# assume that values are not equal in arr
def sort(arr):
    #split arr in two parts ex in 2
    middleIndex = len(arr) // 2
    L = arr[:middleIndex]
    R = arr[middleIndex:]

    #sort both parts
    sort(L)
    sort(R)

    # merge L and R, with invariant condition that L and R are sorted
    # move from lower indexes to higher indexes in L and R and incrementing the 
    # index with the lower corresponding value.
    i = j = k = 0
    # TODO: check cond for optim with and then adding the remaining values
    while i < len(L) or j < len(R) :
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else: 
            arr[k] = R[j]
            j +=1
        k += 1




arr = [1,4,3,8,6,95,12,5]
sort(arr)
print("sorted: ", arr)
