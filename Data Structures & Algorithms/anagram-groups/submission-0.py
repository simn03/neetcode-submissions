class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[int, List[str]] = {}

        for s in strs:
            value: str = "".join(sorted(s))
            hashedVal: int = hash(value)

            if hashedVal not in anagrams:
                anagrams[hashedVal] = []

            anagrams[hashedVal].append(s)

        return list(anagrams.values())