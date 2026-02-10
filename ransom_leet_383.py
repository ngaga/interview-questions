def is_writable(ransomNote, magazine):
    for l in ransomNote:
        if magazine.count(l) < ransomNote.count(l):
            return False
    return True    



ransomNote = "aa"
magazine = "aab"

print(is_writable(ransomNote, magazine))
