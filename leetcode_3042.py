def countPrefixSuffixPairs(words : list[str]) -> int:
    v = [1 for i, vi in enumerate(words) for j, vj in enumerate(words) if i<j and vj.startswith(vi) and vj.endswith(vi)]
    return sum(v)

print(countPrefixSuffixPairs(["a","aba","ababa","aa"]))
# Output: 4
print(countPrefixSuffixPairs(["pa","papa","ma","mama"]))
# Output: 2
print(countPrefixSuffixPairs(["abab","ab"]))
# Output: 0
