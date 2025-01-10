#TODO: make this more efficient.
def isSubset(word : str, potentialSubset : str) -> bool:
    # Make a deep copy
    wordCopy = word[:]
    for i, c in enumerate(potentialSubset):
        if c not in wordCopy:
            return False
        else:
            print(c)
            wordCopy = wordCopy.replace(c,'',1)
            print(wordCopy)
    return True


def isUniversal(word : str, potentialSubsets : list[str]) -> bool:
    return all(isSubset(word, s) for s in potentialSubsets)


def selectUniversal(words : list[str], subsets : list[str]) -> list[str]:
    return [w for w in words if isUniversal(w, subsets)]


# Unittests
# print(isSubset("capres", "scaj"))
# print(isUniversal("capres", ["c", "a", "s"]))

print(selectUniversal(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
# Output: ["facebook","google","leetcode"]
print(selectUniversal(["amazon","apple","facebook","google","leetcode"], ["l","e"]))
# Output: ["apple","google","leetcode"]
print(selectUniversal(["amazon","apple","facebook","google","leetcode"], ["e","oo"]))
# Output ["facebook","google"]
 

