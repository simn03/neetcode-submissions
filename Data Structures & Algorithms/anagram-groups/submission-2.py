class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res: dict[tuple, List[str]] = {}

        for s in strs:
            freqs = [0] * 26

            for c in s:
                n = ord(c) - ord('a')
                freqs[n] += 1

            key = tuple(freqs);

            if (key not in res):
                res[key] = []

            res[key].append(s)

        return list(res.values())