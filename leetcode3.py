#TODO:
def maxLen(s):
  i = 0
  absRes = ""
  tmpRes = ""
  for c in s:
    if c in tmpRes:
      if len(absRes) < len(tmpRes):
        absRes = tmpRes
    else:
      print(f"tmpRes += {c}")
      tmpRes += c
  return absRes

# print("maxLen ", maxLen("abcaxa"))
print("maxLen ", maxLen("pwwkew"))
