def isSubset(word : str, potentialSubset : str) -> bool:
    # TODO: this will not handle multiplicity correctly
    return all(c in word for c in potentialSubset)


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
 

