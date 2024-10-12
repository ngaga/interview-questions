# leetcode 0003
# quadratic O(n2)
def maxLen(s):
  i = 0
  absRes = ""
  for i, unused in enumerate(s):
    tmpRes = ""
    for j, c in enumerate(s[i:len(s)]):
      if c in tmpRes:
        if len(absRes) < len(tmpRes):
          absRes = tmpRes
        tmpRes = ""
      else:
        # print(f"tmpRes += {c}")
        tmpRes += c
  return absRes

# leetcode 0003
# linear O(n)
def maxLenN(s: str) -> int:
    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
        print(s[left:right])

    return max_length  

print("maxLen ", maxLen("abcabcdefbb"))
# print("maxLen ", maxLen("pwwkew"))
# print("maxLen ", maxLen("bbbbbb"))
# print("maxLen ", maxLen(" "))


print("maxLen ", maxLen("abcabcbb"))
print("maxLen ", maxLen("pwwkew"))
print("maxLen ", maxLen("bbbbbb"))
