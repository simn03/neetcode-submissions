class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False;

        letterMap = {}

        for char in s:
            if char in letterMap:
                letterMap[char] += 1
            else:
                letterMap[char] = 1

        for char in t:
            if char not in letterMap:
                return False;

            letterMap[char] -= 1

            if letterMap[char] == 0:
                del letterMap[char]

        if (len(letterMap) > 0):
            return False

        return True;