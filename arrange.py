#import sys
#i = 0
#i = i+1
    #print(i)
    #if i > 10:
    #    sys.exit()

def arrange(remain, build):
    
    if (len(build) == 3):
        print(build)
    else:
        for elements in remain:
            buildCopy = build + remain[-1:]
            remainCopy = remain[:-1]
            arrange(remainCopy, buildCopy)




def arrange2(remain, build):
    if len(build) == 3:
        print(build)
    else:
        for i in range(len(remain)):
            new_build = build + [remain[i]]
            new_remain = remain[:i] + remain[i+1:]
            arrange(new_remain, new_build)
    

arrange2([1, 2, 3], [])
