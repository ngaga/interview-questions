# You are given a 0-indexed string s and a dictionary of words dictionary. 
# You have to break s into one or more non-overlapping substrings such that 
# each substring is present in dictionary. There may be some extra characters 
# in s which are not present in any of the substrings.

# Return the minimum number of extra characters left over if you break up s optimally.

 

# Example 1:

# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and 
# "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

# Example 2:

# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and
#  "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.

import unittest

# check if a word is a part of s
def isPartAtIndex(word, s):
    for i in range(0, len(s) - len(word)):
        if s[i:i+len(word)] == word:
            return
    return None

class TestPart(unittest.TestCase):
    def testPartOne(self):
        

# Solves the exercive above
def extra(s, dictionnary):
    count = 0
    # index for the string s iteration
    i  = 0
    while i < len(s):
        # first test only with the first word of the dictionnary
        a = dictionnary[0]
        while 
        i +=1
        count +=1
    return count


class TestExtra(unittest.TestCase):
    def testOne(self):
        self.assertEqual(extra("leetscode", ["leet","code","leetcode"]), 1)
    def testTwo(self):
        self.assertEqual(extra("sayhelloworld", ["hello","world"]), 3)

if __name__ == '__main__':
    unittest.main()