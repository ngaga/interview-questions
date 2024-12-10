def isSpecial(s : str) -> bool:
    return all(s[i] == s[0] for i in range(len(s))) 

#TODO
def generateSpecialSubstrings(s : str) -> list[str]:
    result = []
    for i in range(len(s)):
        for j in range(len(s)):
            tmp = s[i:j]
            if isSpecial(tmp): 
                result.append(tmp)
    return result 

def isPresentThrice(s : str, substring : str) -> bool:
    count = 0
    for i in range(len(s)):
        if s[i] == substring:
            count = count + 1
    return count >= 3

def getLongestSpecialThrice(input : str) -> int:
    specials = generateSpecialSubstrings(input)
    print("specials ", specials)
    result = -1
    for subStr in specials:
        if isPresentThrice(input, subStr):
            result = max(result, len(subStr))
    return result


print(getLongestSpecialThrice("aaaa"))
print(getLongestSpecialThrice("abcdef"))
print(getLongestSpecialThrice("abcaba"))

# print(isSpecial("abc"))
# print(isSpecial("aa"))
# print(isSpecial("a"))
# print(isSpecial("ccc"))


