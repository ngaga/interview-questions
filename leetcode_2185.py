def countWordsWithPrefix(words : list[str], prefix : str) -> int:
    return sum([1 for word in words if word.startswith(prefix)])


print(
    countWordsWithPrefix(
        ["pay","attention","practice","attend"], "at"
        )
    )
# Output: 2

print(countWordsWithPrefix(["leetcode","win","loops","success"],"code"))
# Output: 0
