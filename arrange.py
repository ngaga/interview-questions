def arrange(remain, build):
    if (len(build) == 3):
        print(build)
    else:
        for i in range(remain):
            arrange(remain - remain[i], build + remain[i])
    

arrange(["a, b, c"], [])
