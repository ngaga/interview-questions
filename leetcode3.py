# leetcode 0003
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

print("maxLen ", maxLen("abcabcbb"))
print("maxLen ", maxLen("pwwkew"))
print("maxLen ", maxLen("bbbbbb"))
