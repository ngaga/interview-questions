def inter(a, b):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return res




a = [1,4,6,8, 65, 88,94,132,999]
b = [1, 2,3,4,5,6,8, 9,  94, 645,999]
c = inter(a, b)
print("instersection", c)
