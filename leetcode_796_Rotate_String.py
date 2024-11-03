def isRotated(s : str, goal : str) -> bool:
  for i in range(0, len(s)):
    s = s[-1] + s[:-1]
    print(s)
    if s == goal:
      return True
  return False

# alternative
def rotateString(s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in s + s

s = "abcde"
goal = "cdeab"
s = "abcde"
goal = "abced"
r = isRotated(s, goal)
print(r)
