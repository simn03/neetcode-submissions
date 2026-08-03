class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[str, List[str]] = {}

        for s in strs:
            value: str = "".join(sorted(s))

            if value not in anagrams:
                anagrams[value] = []

            anagrams[value].append(s)

        return list(anagrams.values())