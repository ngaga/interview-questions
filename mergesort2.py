#takes two sorted arrays and returns the sorted merge
# not in place
def merge(a, b):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        print (i, j)
        print(res)
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < len(a):
        res.append(a[i])
        i += 1
    while j < len(b):
        res.append(b[j])
        j += 1

    return res

#assume that res has allocated size of len(a) + len(b)
def mergeInPlace(a, b, res):
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res[k] = a[i]
            i += 1
        else:
            res[k] = b[j]
            j += 1
        k += 1
    
    while i < len(a):
        res[k] = a[i]
        i += 1
        k += 1
    
    while j < len(b):
        res[k] = b[j]
        j += 1
        k += 1

    


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
        



def test1():
    arr = [99, 1, 4, 2, 9, 54, 6]
    sort(arr)
    print("sorted: ", arr)

def test2():
    a = [1,3]
    b = [2,4]
    m = merge(a, b)
    print("merged: ", m)

def test3():
    a = [1,3, 9, 10, 11]
    b = [2,4]
    r = (len(a) + len(b)) * [0]
    mergeInPlace(a, b, r)
    print("merged", r)

test3()
