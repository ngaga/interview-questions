# assume that values are not equal in arr
def sort(arr):
    # Stopping condition for the reccurence
    # we want at least size 2 to be abble to split
    if len(arr) < 2:
        return

    #split arr in two parts ex in 2
    middleIndex = len(arr) // 2
    L = arr[:middleIndex]
    R = arr[middleIndex:]

    print("middleIndex: ", middleIndex)
    print("L: ", L)
    print("R: ", R)



    #sort both parts
    sort(L)
    sort(R)

    # merge L and R, with invariant condition that L and R are sorted
    # move from lower indexes to higher indexes in L and R and incrementing the 
    # index with the lower corresponding value.
    i = j = k = 0
    # TODO: check cond for optim with and then adding the remaining values
    while i < len(L) and j < len(R):
        print("i ", i, ", j ", j)
        print("L[i] ", L[i], "R[j] ", R[j])
        if L[i] < R[j]:
            print("i push")
            arr[k] = L[i]
            i += 1
        else: 
            print("j push")
            arr[k] = R[j]
            j +=1
        k += 1

    while i < len(L):
        print("i final push")
        arr[k] = L[i]
        i += 1
        k +=1

    while j < len(R):
        print("j final push")
        arr[k] = R[j]
        j += 1
        k +=1
        



# test main
arr = [99, 1, 4, 2, 9, 54, 6]
sort(arr)
print("sorted: ", arr)
