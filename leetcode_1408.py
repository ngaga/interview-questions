def isWordInList(wordList : list[str], target : str) -> Bool:
    for w in wordList:
        if target in w:
            return True
    return False

def wordInOthers(wordList : list[str]) -> list[str]:
    result = []
    for word in wordList:
        listExtract = wordList[:]
        listExtract.remove(word)
        
    return result


print
# print(wordInOthers(["mass","as","hero","superhero"]))
# Output: ["as","hero"]
