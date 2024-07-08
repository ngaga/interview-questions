#import sys
#i = 0
#i = i+1
    #print(i)
    #if i > 10:
    #    sys.exit()

def arrange(remain, build):
    
    if (not remain):
        print(build)
    else:
        for i in range(len(remain)):
            #print ("i ", i)
            buildCopy = build + [remain[i]]
            #print ("buildCopy ",buildCopy)
            remainCopy = remain.copy() #BE CAREFULL OF THE COPY HERE :)
            #print ("remaincopy",remainCopy)
            del remainCopy[i]
            #print ("remaincopydel ",remainCopy)
            #print(buildCopy, remainCopy)
            arrange(remainCopy, buildCopy)




    

arrange([1, 2, 3, 4], [])
