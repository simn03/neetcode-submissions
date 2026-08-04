class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0

        chars = {}

        for i, c in enumerate(s):

            if c in chars:
                if chars[c] >= start:
                    start = chars[c] + 1
                del chars[c]

            chars[c] = i

            longest = max(longest, i - start + 1)

        return longest
