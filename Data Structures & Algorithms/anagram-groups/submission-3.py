class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res: dict[tuple, List[str]] = defaultdict(list)

        for s in strs:
            freqs = [0] * 26

            for c in s:
                n = ord(c) - ord('a')
                freqs[n] += 1

            key = tuple(freqs);

            res[key].append(s)

        return list(res.values())