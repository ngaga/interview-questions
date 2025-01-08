def isWordInList(wordList : list[str], target : str) -> bool:
    for w in wordList:
        if target in w:
            return True
    return False

def wordInOthers(wordList : list[str]) -> list[str]:
    result = []
    for word in wordList:
        listExtract = wordList.copy()
        listExtract.remove(word)
        if isWordInList(listExtract, word):
            result.append(word)   
    return result


print(wordInOthers(["mass","as","hero","superhero"]))
# Output: ["as","hero"]
print(wordInOthers(["leetcode","et","code"]))
# Output: ["et","code"]
print(wordInOthers(["blue","green","bu"]))
# Output: []
